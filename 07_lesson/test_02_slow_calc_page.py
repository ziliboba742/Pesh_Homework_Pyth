import pytest
from selenium import webdriver
from pages.SlowCalcPage import SlowCalculatorPage
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator_flow(driver):
    calc = SlowCalculatorPage(driver)
    calc.open()

    calc.set_delay("45")

    calc.press_button('7')
    calc.press_button('+')
    calc.press_button('8')
    calc.press_button('=')

    result = calc.get_result(timeout=60, expected_text='15')

    assert result == '15'
