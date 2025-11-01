# test_03_shop.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
import re

def test_sauce_demo_checkout():
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    try:
        driver.get("https://www.saucedemo.com/")
        wait = WebDriverWait(driver, 20)

        user = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        user.send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        to_add = [
            "add-to-cart-sauce-labs-backpack",
            "add-to-cart-sauce-labs-bolt-t-shirt",
            "add-to-cart-sauce-labs-onesie",
        ]
        for data_test in to_add:
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"[data-test='{data_test}']"))).click()

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shopping_cart_link"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        wait.until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys("John")
        driver.find_element(By.ID, "last-name").send_keys("Doe")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        driver.find_element(By.ID, "continue").click()

        total_el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".summary_total_label")))
        text = total_el.text
        m = re.search(r"\$([0-9]+(?:\.[0-9]{2})?)", text)
        assert m is not None
        total_value = float(m.group(1))
        assert abs(total_value - 58.29) < 0.001
    finally:
        driver.quit()
