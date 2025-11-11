from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart_by_name(self, product_name: str, timeout: int = 10):
        items = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME,
                                                 "inventory_item"))
        )
        for item in items:
            title = item.find_element(
                By.CLASS_NAME, "inventory_item_name"
                ).text
            if title.strip() == product_name:
                add_button = item.find_element(
                    By.CSS_SELECTOR, "button.btn_primary.btn_inventory"
                    )
                WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable(add_button)
                ).click()
                return

    def go_to_cart(self, timeout: int = 10):
        cart_button = (By.CLASS_NAME, "shopping_cart_link")
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(cart_button)
        ).click()
