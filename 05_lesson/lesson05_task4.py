from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
)

driver.get("http://the-internet.herokuapp.com/login")
sleep(1)

driver.find_element(By.ID, "username").send_keys("tomsmith")
sleep(1)

driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
sleep(1)

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

wait = WebDriverWait(driver, 10)
message_element = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash"))
)

sleep(1)
print(message_element.text)
sleep(1)

driver.quit()
