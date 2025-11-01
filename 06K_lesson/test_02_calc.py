# test_02_calc.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def _click_button_three_strategies(driver: webdriver.Chrome, label: str, timeout: int = 20) -> None:
    wait = WebDriverWait(driver, timeout)

    span_xpath = f"//span[contains(@class, 'btn') and normalize-space()='{label}']"
    try:
        span_btn = wait.until(EC.element_to_be_clickable((By.XPATH, span_xpath)))
        span_btn.click()
        return
    except Exception:
        pass

    button_with_span_xpath = (
        f"//button[.//span[contains(@class, 'btn') and normalize-space()='{label}']]"
    )
    try:
        btn_with_span = wait.until(EC.element_to_be_clickable((By.XPATH, button_with_span_xpath)))
        btn_with_span.click()
        return
    except Exception:
        pass

    text_button_xpath = f"//button[normalize-space()='{label}']"
    try:
        btn_by_text = wait.until(EC.element_to_be_clickable((By.XPATH, text_button_xpath)))
        btn_by_text.click()
        return
    except Exception:
        pass

    raise Exception(f"Button '{label}' not clickable via any strategy")


def test_slow_calculator_addition():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        wait = WebDriverWait(driver, 20)

        delay_el = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#delay")))
        delay_el.clear()
        delay_el.send_keys("45")

        for label in ["7", "+", "8", "="]:
            _click_button_three_strategies(driver, label)

        screen_locator = (By.CSS_SELECTOR, ".screen")
        WebDriverWait(driver, 120).until(EC.text_to_be_present_in_element(screen_locator, "15"))
        screen_el = wait.until(EC.presence_of_element_located(screen_locator))
        value = screen_el.get_attribute("value") if screen_el.tag_name.lower() == "input" else screen_el.text
        assert "15" in value.strip()
    finally:
        driver.quit()