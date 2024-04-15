import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def chrome_options():
    options = Options()
    options.add_argument("--window-size=1500, 900")
    # options.add_argument("--headless")
    return options

def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# DATA
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

# LOCATORS
START_TEST_BTN = ("xpath", "//button[@id='startTest']")
H1 = ("xpath", "//h1")
LOGIN_FIELD = ("xpath", '//input[@id="login"]')
PASSWORD_FIELD = ("xpath", '//input[@id="password"]')
REGISTER_BTN = ("xpath", "//button[@id='register']")

# URLS
URL_MAIN_PAGE = "https://victoretc.github.io/selenium_waits/"

def test_implisit(driver):
    driver.get(URL_MAIN_PAGE)
    h1_text = driver.find_element(*H1).text
    assert h1_text == "Практика с ожиданиями в Selenium", "не соответствует тексту в теге h1"
    driver.find_element(*START_TEST_BTN).click()
    driver.find_element(*LOGIN_FIELD).send_keys(LOGIN)
    driver.find_element(*PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(*REGISTER_BTN).click()
    time.sleep(6)






