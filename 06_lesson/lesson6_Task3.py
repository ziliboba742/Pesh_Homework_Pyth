from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get(
    'https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

wait = WebDriverWait(driver, 15)

container = wait.until(
    EC.presence_of_element_located((By.ID, "image-container"))
)

images = wait.until(
    lambda driver: len(container.find_elements(By.TAG_NAME, "img")) >= 4
)

images_list = container.find_elements(By.TAG_NAME, "img")
src_third_image = images_list[2].get_attribute('src')
print(src_third_image)


driver.quit()
