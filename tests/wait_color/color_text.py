import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    chrom_options = webdriver.ChromeOptions()
    # chrom_options.add_argument("--incognito")
    chrom_options.add_argument('--window-size=100,100')
    # chrom_options.add_argument('--headless')
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrom_options)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=15)
    return wait



BTN_COLOR = ("xpath", '//button[contains(@class, "text-danger")]')

def test_color_text(driver, wait):
    driver.get('https://demoqa.com/dynamic-properties')
    button = wait.until(EC.visibility_of_element_located(BTN_COLOR))
    color = button.value_of_css_property("color")
    assert color == "rgba(220, 53, 69, 1)"
    print(color)

