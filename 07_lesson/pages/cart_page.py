from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self, timeout: int = 10):
        checkout_btn = (By.ID, "checkout")
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(checkout_btn)
        ).click()
