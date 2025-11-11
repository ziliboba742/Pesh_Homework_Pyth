from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def get_total(self, timeout: int = 10) -> float:
        selectors = [
            (By.ID, "summary_total_label"),
            (By.ID, "total_label"),
            (By.CLASS_NAME, "summary_total_label"),
            (By.CSS_SELECTOR, ".summary_total_label"),
        ]
        for by, locator in selectors:
            try:
                el = WebDriverWait(self.driver, 5).until(
                    EC.visibility_of_element_located((by, locator))
                )
                text = el.text
                m = re.search(r"\$?([0-9]+(?:\.[0-9]{2}))", text)
                if m:
                    return float(m.group(1))
            except Exception:
                continue

    def click_finish(self, timeout: int = 10):
        finish_button = (By.ID, "finish")
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(finish_button)
        ).click()
