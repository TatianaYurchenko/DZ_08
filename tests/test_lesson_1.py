import time
import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select



chrom_options = webdriver.ChromeOptions()
chrom_options.add_argument("--headless")
chrom_options.add_argument("--window-size=1500, 900")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrom_options)
wait = WebDriverWait(driver, timeout=15)
action = ActionChains(driver)

URL_LOGIN_PAGE = "https://www.saucedemo.com/"
URL_INVENTORY_PAGE = "https://www.saucedemo.com/inventory.html"
URL_CARD_PAGE = "https://www.saucedemo.com/cart.html"
URL_CHECKOUT_PAGE = "https://www.saucedemo.com/checkout-step-one.html"
URL_CHECKOUT_PAGE_STEP_TWO = "https://www.saucedemo.com/checkout-step-two.html"

LOGIN_FIELD = ("xpath", '//input[@id="user-name"]')
PASSWORD_FIELD = ("xpath", '//input[@id="password"]')
lOGIN_BTN = ("xpath", '//input[@type="submit"]')
LOGIN_ERROR_MESSAGE = ("xpath", '//h3[@data-test="error"]')
BURGER_MENU = ("xpath", '//button[@id="react-burger-menu-btn"]')
LOGOUT = ("xpath", '//a[@id="logout_sidebar_link"]')
ADD_TO_CARD_BTM = ("xpath", '(//button[contains(@class,"btn")])[1]')
ADD_TO_CARD_BTM_IN_INVENTORY_DTL = ("xpath", '(//button[contains(@class,"btn")])[2]')
CARD = ("xpath", '//div[@id="shopping_cart_container"]')
ITEM_NAME = ("xpath", '(//div[@class="inventory_item_name "])[1]')
ITEM_TITLE_LINK = ("xpath", '//a[@id="item_4_title_link"]')
ITEM_IMG_LINK = ("xpath", '//a[@id="item_4_img_link"]')
ITEM_NAME_IN_CARD = ("xpath", '(//div[@class="inventory_item_name"])[1]')
INVENTORY_NAME = ("xpath", '//div[contains(@class, "large_size")]')
CHECKOUT_BTN = ("xpath", '//button[contains(@class,"checkout_button ")]')
FERST_NAME = ("xpath", '//input[@id="first-name"]')
lAST_NAME = ("xpath", '//input[@id="last-name"]')
ZIP = ("xpath", '//input[@id="postal-code"]')
CONTINUE_BTN = ("xpath", '//input[@id="continue"]')
FINISH_BTN = ("xpath", '//button[@id="finish"]')
THANK_TEXT = ("xpath", '//h2[@class="complete-header"]')
DROPDOWN_ELEMENT = ("xpath", '//select[@class="product_sort_container"]')



# Авторизация
def auth_positive():
    driver.get(URL_LOGIN_PAGE)
    driver.find_element(*LOGIN_FIELD).send_keys('standard_user')
    driver.find_element(*PASSWORD_FIELD).send_keys('secret_sauce')
    driver.find_element(*lOGIN_BTN).click()
    assert driver.current_url == URL_INVENTORY_PAGE, "Unexpected page URL"

def test_auth_negativ():
    driver.get(URL_LOGIN_PAGE)
    driver.find_element(*LOGIN_FIELD).send_keys('user')
    driver.find_element(*PASSWORD_FIELD).send_keys('user')
    driver.find_element(*lOGIN_BTN).click()
    assert driver.find_element(*LOGIN_ERROR_MESSAGE).text == "Epic sadface: Username and password do not match any user in this service"

def test_auth_positive():
    auth_positive()
    # driver.find_element(*BURGER_MENU).click()
    # action.move_to_element(wait.until(EC.visibility_of_element_located(LOGOUT))).click().perform()

# Карточка товара
def test_move_on_inventory_details_by_img():
    auth_positive()
    text_of_item_name = driver.find_element(*ITEM_NAME).text
    wait.until(EC.element_to_be_clickable(ITEM_IMG_LINK)).click()
    a = wait.until(EC.element_to_be_clickable(INVENTORY_NAME)).text
    assert text_of_item_name == a

def test_move_on_inventory_details_by_title():
    auth_positive()
    text_of_item_name = driver.find_element(*ITEM_NAME).text
    wait.until(EC.element_to_be_clickable(ITEM_TITLE_LINK)).click()
    a = wait.until(EC.element_to_be_clickable(INVENTORY_NAME)).text
    assert text_of_item_name == a


# Корзина
def element_is_invisibility(loc):
    wait.until(EC.element_to_be_clickable(ADD_TO_CARD_BTM)).click()
    assert EC.invisibility_of_element(loc)

def test_add_good():
    auth_positive()
    text_of_item_name = driver.find_element(*ITEM_NAME).text
    wait.until(EC.element_to_be_clickable(ADD_TO_CARD_BTM)).click()
    driver.get(URL_CARD_PAGE)
    assert driver.current_url == URL_CARD_PAGE, 'Wrong URL'
    a = wait.until(EC.element_to_be_clickable(ITEM_NAME_IN_CARD)).text
    assert text_of_item_name == a
    wait.until(EC.element_to_be_clickable(ADD_TO_CARD_BTM)).click()

def test_delete_good():
    auth_positive()
    text_of_item_name = driver.find_element(*ITEM_NAME).text
    wait.until(EC.element_to_be_clickable(ADD_TO_CARD_BTM)).click()
    driver.get(URL_CARD_PAGE)
    assert driver.current_url == URL_CARD_PAGE, 'Wrong URL'
    a = wait.until(EC.element_to_be_clickable(ITEM_NAME_IN_CARD)).text
    assert text_of_item_name == a
    wait.until(EC.element_to_be_clickable(ADD_TO_CARD_BTM)).click()
    element_is_invisibility(ITEM_NAME_IN_CARD)

def test_add_good_from_inventory_details():
    auth_positive()
    text_of_item_name = driver.find_element(*ITEM_NAME).text
    wait.until(EC.element_to_be_clickable(ITEM_TITLE_LINK)).click()
    wait.until(EC.element_to_be_clickable(ADD_TO_CARD_BTM_IN_INVENTORY_DTL)).click()
    driver.get(URL_CARD_PAGE)
    assert driver.current_url == URL_CARD_PAGE, 'Wrong URL'
    a = wait.until(EC.element_to_be_clickable(ITEM_NAME_IN_CARD)).text
    assert text_of_item_name == a
    wait.until(EC.element_to_be_clickable(ADD_TO_CARD_BTM)).click()

def test_delete_good_from_inventory_details():
    test_add_good_from_inventory_details()
    element_is_invisibility(ITEM_NAME_IN_CARD)

#     Оформление заказа

def test_make_order():
    auth_positive()
    text_of_item_name = driver.find_element(*ITEM_NAME).text
    wait.until(EC.element_to_be_clickable(ADD_TO_CARD_BTM)).click()
    driver.find_element(*CARD).click()
    assert driver.current_url == URL_CARD_PAGE, 'Wrong URL'
    a = wait.until(EC.element_to_be_clickable(ITEM_NAME_IN_CARD)).text
    assert text_of_item_name == a
    driver.find_element(*CHECKOUT_BTN).click()
    assert driver.current_url == URL_CHECKOUT_PAGE, 'Wrong URL'
    driver.find_element(*FERST_NAME).send_keys('Tatiana')
    driver.find_element(*lAST_NAME).send_keys('Tatiana')
    driver.find_element(*ZIP).send_keys('1236')
    driver.find_element(*CONTINUE_BTN).click()
    assert driver.current_url == URL_CHECKOUT_PAGE_STEP_TWO, 'Wrong URL'
    driver.find_element(*FINISH_BTN).click()
    assert driver.find_element(*THANK_TEXT).text == "Thank you for your order!"

# Фильтр

def test_filtr_a_z():
    auth_positive()
    before = driver.find_elements('xpath', '//div[@class="inventory_item_name "]')
    lst1 = []
    lst2 = []
    for i in before:
        lst1.append(i.text)
    sorted_lst1 = sorted(lst1)
    DROPDOWN = Select(driver.find_element(*DROPDOWN_ELEMENT))
    DROPDOWN.select_by_index(0)
    after = driver.find_elements('xpath', '//div[@class="inventory_item_name "]')
    for j in after:
        lst2.append(j.text)
    assert lst2 == sorted_lst1

def test_filtr_z_a():
    auth_positive()
    before = driver.find_elements('xpath', '//div[@class="inventory_item_name "]')
    lst1 = []
    lst2 = []
    for i in before:
        lst1.append(i.text)
    sorted_lst1 = sorted(lst1, reverse=True)
    DROPDOWN = Select(driver.find_element(*DROPDOWN_ELEMENT))
    DROPDOWN.select_by_index(1)
    after = driver.find_elements('xpath', '//div[@class="inventory_item_name "]')
    for j in after:
        lst2.append(j.text)
    assert lst2 == sorted_lst1

def test_filtr_low_high():
    auth_positive()
    before = driver.find_elements('xpath', '//div[@class="inventory_item_price"]')
    lst1 = []
    lst2 = []
    for i in before:
        i = i.text
        i = i[1:]
        lst1.append(float(i))
    sorted_lst1 = sorted(lst1)
    print(sorted_lst1)
    DROPDOWN = Select(driver.find_element(*DROPDOWN_ELEMENT))
    DROPDOWN.select_by_index(2)
    after = driver.find_elements('xpath', '//div[@class="inventory_item_price"]')
    for j in after:
        j = j.text
        j = j[1:]
        lst2.append(float(j))
    print(lst2)
    assert lst2 == sorted_lst1

def test_filtr_high_low():
    auth_positive()
    before = driver.find_elements('xpath', '//div[@class="inventory_item_price"]')
    lst1 = []
    lst2 = []
    for i in before:
        i = i.text
        i = i[1:]
        lst1.append(float(i))
    sorted_lst1 = sorted(lst1, reverse=True)
    print(sorted_lst1)
    DROPDOWN = Select(driver.find_element(*DROPDOWN_ELEMENT))
    DROPDOWN.select_by_index(3)
    after = driver.find_elements('xpath', '//div[@class="inventory_item_price"]')
    for j in after:
        j = j.text
        j = j[1:]
        lst2.append(float(j))
    print(lst2)
    assert lst2 == sorted_lst1




def test_2():
    auth_positive()
    hr = ("xpath", '//a[@id="item_4_title_link"]')
    element = driver.find_element(*hr)
    link = element.get_attribute('href')
    print(link)


# def test_add_goods():
#     test_auth_positive()
#     text_of_btm = driver.find_element(*ADD_TO_CARD_BTM).text
#     print(text_of_btm)
#     text_of_item_name = driver.find_element(*INVENTORY_ITEM_NAME).text
#     print(text_of_item_name )
#     if text_of_btm == 'Add to cart':
#         wait.until(EC.element_to_be_clickable(ADD_TO_CARD_BTM)).click()
#         time.sleep(3)
#         driver.find_element(*ADD_TO_CARD_BTM).click()
#         driver.find_element(*CARD).click()
#
#         time.sleep(2)
#     elif text_of_btm == 'Remove':
#         driver.find_element(*CARD).click()
#     else:
#         print('Error text of the add to card button')
#     assert driver.current_url == URL_CARD_PAGE, 'Wrong URL'
#     time.sleep(2)
#     a = wait.until(EC.element_to_be_clickable(INVENTORY_ITEM_NAME_IN_CARD)).text
#     assert text_of_item_name == a
#     print(a)
#     print(driver.find_element(*INVENTORY_ITEM_NAME_IN_CARD).text)
#     # print(a)



