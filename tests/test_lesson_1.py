import time
import pytest

from tests.data import *
from tests.locators import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select



# Авторизация
def auth_positive(driver):
    driver.get(URL_LOGIN_PAGE)
    driver.find_element(*LOGIN_FIELD).send_keys(LOGIN)
    driver.find_element(*PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(*lOGIN_BTN).click()
    assert driver.current_url == URL_INVENTORY_PAGE, "Unexpected page URL"

def test_auth_negativ(driver):
    driver.get(URL_LOGIN_PAGE)
    driver.find_element(*LOGIN_FIELD).send_keys(LOGIN_NEGATIVE)
    driver.find_element(*PASSWORD_FIELD).send_keys(PASSWORD_NEGATIVE)
    driver.find_element(*lOGIN_BTN).click()
    assert driver.find_element(*LOGIN_ERROR_MESSAGE).text == "Epic sadface: Username and password do not match any user in this service"

def test_auth_positive(driver):
    auth_positive(driver)

# Карточка товара
def test_move_on_inventory_details_by_img(driver, wait):
    auth_positive(driver)
    text_of_item_name = driver.find_element(*ITEM_NAME).text
    wait.until(EC.element_to_be_clickable(ITEM_IMG_LINK)).click()
    a = wait.until(EC.element_to_be_clickable(INVENTORY_NAME)).text
    assert text_of_item_name == a

def test_move_on_inventory_details_by_title(driver, wait):
    auth_positive(driver)
    text_of_item_name = driver.find_element(*ITEM_NAME).text
    wait.until(EC.element_to_be_clickable(ITEM_TITLE_LINK)).click()
    a = wait.until(EC.element_to_be_clickable(INVENTORY_NAME)).text
    assert text_of_item_name == a


# Корзина
def element_is_invisibility(loc, wait):
    wait.until(EC.element_to_be_clickable(ADD_TO_CARD_BTM)).click()
    assert EC.invisibility_of_element(loc)

def test_add_good(driver, wait):
    auth_positive(driver)
    text_of_item_name = driver.find_element(*ITEM_NAME).text
    wait.until(EC.element_to_be_clickable(ADD_TO_CARD_BTM)).click()
    driver.find_element(*CARD).click()
    assert driver.current_url == URL_CARD_PAGE, 'Wrong URL'
    a = wait.until(EC.element_to_be_clickable(ITEM_NAME_IN_CARD)).text
    assert text_of_item_name == a, 'Product is missing in the cart'
    wait.until(EC.element_to_be_clickable(ADD_TO_CARD_BTM)).click()

def test_delete_good(driver, wait):
    auth_positive(driver)
    text_of_item_name = driver.find_element(*ITEM_NAME).text
    wait.until(EC.element_to_be_clickable(ADD_TO_CARD_BTM)).click()
    driver.find_element(*CARD).click()
    assert driver.current_url == URL_CARD_PAGE, 'Wrong URL'
    a = wait.until(EC.element_to_be_clickable(ITEM_NAME_IN_CARD)).text
    assert text_of_item_name == a, 'Product wasn\'t removed from the cart'
    element_is_invisibility(ITEM_NAME_IN_CARD, wait)
    assert not driver.find_elements('xpath', '//*[@id="item_4_title_link"]'), 'Product wasn\'t removed from the cart'

def test_add_good_from_inventory_details(driver, wait):
    auth_positive(driver)
    text_of_item_name = driver.find_element(*ITEM_NAME).text
    wait.until(EC.element_to_be_clickable(ITEM_TITLE_LINK)).click()
    wait.until(EC.element_to_be_clickable(ADD_TO_CARD_BTM_IN_INVENTORY_DTL)).click()
    driver.find_element(*CARD).click()
    assert driver.current_url == URL_CARD_PAGE, 'Wrong URL'
    a = wait.until(EC.element_to_be_clickable(ITEM_NAME_IN_CARD)).text
    assert text_of_item_name == a, 'Product is missing in the cart'
    wait.until(EC.element_to_be_clickable(ADD_TO_CARD_BTM)).click()

def test_delete_good_from_inventory_details(driver, wait):
    test_add_good_from_inventory_details(driver, wait)
    element_is_invisibility(ITEM_NAME_IN_CARD, wait)

#     Оформление заказа

def test_make_order(driver,wait):
    auth_positive(driver)
    text_of_item_name = driver.find_element(*ITEM_NAME).text
    wait.until(EC.element_to_be_clickable(ADD_TO_CARD_BTM)).click()
    driver.find_element(*CARD).click()
    assert driver.current_url == URL_CARD_PAGE, 'Wrong URL'
    a = wait.until(EC.element_to_be_clickable(ITEM_NAME_IN_CARD)).text
    assert text_of_item_name == a
    driver.find_element(*CHECKOUT_BTN).click()
    assert driver.current_url == URL_CHECKOUT_PAGE, 'Wrong URL'
    driver.find_element(*FERST_NAME).send_keys(FERST_NAME)
    driver.find_element(*lAST_NAME).send_keys(LAST_NAME)
    driver.find_element(*ZIP).send_keys(ZIP)
    driver.find_element(*CONTINUE_BTN).click()
    assert driver.current_url == URL_CHECKOUT_PAGE_STEP_TWO, 'Wrong URL'
    driver.find_element(*FINISH_BTN).click()
    assert driver.find_element(*THANK_TEXT).text == "Thank you for your order!"

# Фильтр

def test_filtr_a_z(driver):
    auth_positive(driver)
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

def test_filtr_z_a(driver):
    auth_positive(driver)
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

def test_filtr_low_high(driver):
    auth_positive(driver)
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

def test_filtr_high_low(driver):
    auth_positive(driver)
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

# Бургер меню
def test_logout(driver, wait):
    action = ActionChains(driver)
    auth_positive(driver)
    driver.find_element(*BURGER_MENU).click()
    action.move_to_element(wait.until(EC.visibility_of_element_located(LOGOUT))).click().perform()
    assert driver.current_url == URL_LOGIN_PAGE, 'Wrong URL'

def test_About_btm(driver, wait):
    action = ActionChains(driver)
    auth_positive(driver)
    driver.find_element(*BURGER_MENU).click()
    action.move_to_element(wait.until(EC.visibility_of_element_located(ABOUT))).click().perform()
    assert driver.current_url == URL_ABOUT_PAGE, 'Wrong URL'

def test_2(driver):
    auth_positive(driver)
    hr = ("xpath", '//a[@id="item_4_title_link"]')
    element = driver.find_element(*hr)
    link = element.get_attribute('href')
    print(link)




