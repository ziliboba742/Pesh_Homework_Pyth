from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")
driver.find_element(By.CSS_SELECTOR, "input#newButtonName").send_keys("SkyPro")
button = driver.find_element(By.CSS_SELECTOR, "button#updatingButton")
button.click()

print(button.text)

driver.quit()
