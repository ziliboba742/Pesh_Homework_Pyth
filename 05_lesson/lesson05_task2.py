from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.get("http://uitestingplayground.com/dynamicid")
driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()

sleep(3)

driver.quit()
