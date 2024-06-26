import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    chrom_options = webdriver.ChromeOptions()
    chrom_options.add_argument("--incognito")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrom_options)
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=15)
    return wait


# DATA
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

# LOCATORS
START_TEST_BTN = ("xpath", "//button[@id='startTest']")
H1 = ("xpath", "//h1")
LOGIN_FIELD = ("xpath", '//input[@id="login"]')
PASSWORD_FIELD = ("xpath", '//input[@id="password"]')
REGISTER_BTN = ("xpath", "//button[@id='register']")
CHECKBOX = ("xpath", "//input[@type='checkbox']")
SUCCESS_MESSAGE = ("xpath", "//p[@id='successMessage']")
LOADER = ("xpath", "//div[@id='loader']")
# URLS
URL_MAIN_PAGE = "https://victoretc.github.io/selenium_waits/"


def test_explisit(driver, wait):
    driver.get(URL_MAIN_PAGE)
    h1_text = driver.find_element(*H1).text
    assert h1_text == "Практика с ожиданиями в Selenium", "не соответствует тексту в теге h1"
    wait.until(EC.element_to_be_clickable(START_TEST_BTN)).click()
    driver.find_element(*LOGIN_FIELD).send_keys(LOGIN)
    driver.find_element(*PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(*CHECKBOX).click()
    driver.find_element(*REGISTER_BTN).click()
    loader_text = wait.until(EC.visibility_of_element_located(LOADER)).text
    assert loader_text =='Загрузка...'
    success_text = wait.until(EC.element_to_be_clickable(SUCCESS_MESSAGE)).text
    assert success_text == 'Вы успешно зарегистрированы!'



# allow pasting
# setTimeout(function(){debugger;}, 3000)
