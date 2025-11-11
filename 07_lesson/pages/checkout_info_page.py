from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutInfoPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

    def enter_first_name(self, first_name: str, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.first_name)
        ).send_keys(first_name)

    def enter_last_name(self, last_name: str, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.last_name)
        ).send_keys(last_name)

    def enter_postal_code(self, postal_code: str, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.postal_code)
        ).send_keys(postal_code)

    def click_continue(self, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()
