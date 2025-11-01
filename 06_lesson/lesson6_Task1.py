from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)

driver.get("http://uitestingplayground.com/ajax")
load_button = driver.find_element(By.CSS_SELECTOR, "button#ajaxButton")
load_button.click()

green_message = driver.find_element(By.CSS_SELECTOR, ".bg-success")
print(green_message.text)

driver.quit()
