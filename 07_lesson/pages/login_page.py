from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self, username: str, password: str, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.password_input)
        ).send_keys(password)
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.login_button)
        ).click()
