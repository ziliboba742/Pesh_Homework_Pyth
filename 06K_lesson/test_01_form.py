from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EDGE_DRIVER_PATH = r"Z:\web_driver_edge\msedgedriver.exe"


def parse_rgb_no_regex(color_str):
    if not color_str:
        return None
    s = color_str.strip().lower()
    if not ((s.startswith("rgb(") and s.endswith(")")) or
            (s.startswith("rgba(") and s.endswith(")"))):
        return None
    inner = s[s.find("(") + 1 : -1]
    parts = [p.strip() for p in inner.split(",")]
    if len(parts) < 3:
        return None
    try:
        r = int(parts[0])
        g = int(parts[1])
        b = int(parts[2])
        return r, g, b
    except ValueError:
        return None


def is_red(color_str):
    rgb = parse_rgb_no_regex(color_str)
    if not rgb:
        return False
    r, g, b = rgb
    return (r > g) and (r > b) and ((r - min(g, b)) >= 20)


def is_green(color_str):
    rgb = parse_rgb_no_regex(color_str)
    if not rgb:
        return False
    r, g, b = rgb
    return (g > r) and (g > b) and ((g - min(r, b)) >= 20)


def input_by_name(driver, wait, name, value):
    el = wait.until(EC.presence_of_element_located((By.NAME, name)))
    el.clear()
    if value:
        el.send_keys(value)
    return el


def test_form_validation_in_edge():
    options = Options()
    options.use_chromium = True
    service = Service(executable_path=EDGE_DRIVER_PATH)
    driver = webdriver.Edge(service=service, options=options)
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        fields = [
            ("first-name", "Иван"),
            ("last-name", "Петров"),
            ("address", "Ленина, 55-3"),
            ("e-mail", "test@skypro.com"),
            ("phone", "+7985899998787"),
            ("zip-code", ""),
            ("city", "Москва"),
            ("country", "Россия"),
            ("job-position", "QA"),
            ("company", "SkyPro"),
        ]

        for name, value in fields:
            input_by_name(driver, wait, name, value)

        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='submit']")))
        submit.click()

        after_inputs = {}
        for name, _ in fields:
            el = wait.until(EC.presence_of_element_located((By.ID, name)))
            after_inputs[name] = el

        zip_color = after_inputs["zip-code"].value_of_css_property("border-color")
        assert is_red(zip_color), f"Zip code border-color должен быть красным, получил {zip_color}"

        for name, _ in fields:
            if name == "zip-code":
                continue
            color = after_inputs[name].value_of_css_property("border-color")
            assert is_green(color), f"Поле {name} обводка должна быть зелёной, получила {color}"

    finally:
        driver.quit()
