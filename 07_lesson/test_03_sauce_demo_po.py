from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage


def test_sauce_demo_page_object_pattern():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    try:
        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_to_cart_by_name("Sauce Labs Backpack")
        inventory.add_to_cart_by_name("Sauce Labs Bolt T-Shirt")
        inventory.add_to_cart_by_name("Sauce Labs Onesie")

        inventory.go_to_cart()

        cart = CartPage(driver)
        cart.click_checkout()

        info = CheckoutInfoPage(driver)
        info.enter_first_name("John")
        info.enter_last_name("Doe")
        info.enter_postal_code("12345")
        info.click_continue()

        overview = CheckoutOverviewPage(driver)
        total = overview.get_total()

        driver.quit()

        assert abs(total - 58.29) < 0.01, f"Expected total 58.29, got {total}"
    finally:

        driver.quit()
