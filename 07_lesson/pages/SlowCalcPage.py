import time
from selenium.webdriver.common.by import By


class SlowCalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, seconds):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        delay_input.clear()
        delay_input.send_keys(seconds)

    def press_button(self, label):
        if label in '0123456789.':
            buttons = self.driver.find_elements(
                By.CSS_SELECTOR, "div.keys span.btn.btn-outline-primary"
                )
            for btn in buttons:
                if btn.text.strip() == label:
                    btn.click()
                    return

        elif label in ['+', '-', '÷', 'x']:
            operator_buttons = self.driver.find_elements(
                By.CSS_SELECTOR,
                "div.keys span.operator.btn.btn-outline-success"
                )
            for btn in operator_buttons:
                if btn.text.strip() == label:
                    btn.click()
                    return

        elif label == '=':
            equals_buttons = self.driver.find_elements(
                By.CSS_SELECTOR, "div.keys span.btn.btn-outline-warning"
                )
            for btn in equals_buttons:
                if btn.text.strip() == label:
                    btn.click()
                    return

    def get_result(self, timeout=60, expected_text=None):
        end_time = time.time() + timeout
        while time.time() < end_time:
            text = self.driver.find_element(
                By.CSS_SELECTOR, "div.screen").text.strip()
            if expected_text is not None:
                if text == expected_text:
                    return text
            else:
                if text != "":
                    return text
        return text
