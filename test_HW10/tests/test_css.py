import time
import allure
from selenium.webdriver.common.by import By

URL_WB = 'https://www.wildberries.by/'


@allure.suite("Locators")
@allure.sub_suite("CSS")
@allure.title("Banner_is_present")
def test_css_banner_is_present(driver):
    driver.get(URL_WB)
    element = driver.find_element(By.CSS_SELECTOR, 'div.main-page__banner.banner')
    time.sleep(10)
    assert element.is_displayed()

@allure.suite("Locators")
@allure.sub_suite("CSS")
@allure.title("Currency_icon_is_present")
def test_css_currency_icon_is_present(driver):
    driver.get(URL_WB)
    element = driver.find_element(By.CSS_SELECTOR, 'span.simple-menu__currency')
    time.sleep(5)
    assert element.is_displayed()

@allure.suite("Locators")
@allure.sub_suite("CSS")
@allure.title("Navigation_menu_is_present")
def test_css_navigation_menu_is_present(driver):
    driver.get(URL_WB)
    element = driver.find_element(By.CSS_SELECTOR, 'button[class*="burger"]')
    assert element.is_displayed()

@allure.suite("Locators")
@allure.sub_suite("CSS")
@allure.title("Search_field_is_present")
def test_css_search_field_is_present(driver):
    driver.get(URL_WB)
    element = driver.find_element(By.CSS_SELECTOR, 'div#searchBlock')
    assert element.is_displayed()

@allure.suite("Locators")
@allure.sub_suite("CSS")
@allure.title("Site_logo_is_present")
def test_css_site_logo_is_present(driver):
    driver.get(URL_WB)
    element = driver.find_element(By.CSS_SELECTOR, 'a[class*="nav-element__logo"]')
    assert element.is_displayed()

@allure.suite("Locators")
@allure.sub_suite("CSS")
@allure.title("Basket_is_present")
def test_css_basket_is_present(driver):
    driver.get(URL_WB)
    element = driver.find_element(By.CSS_SELECTOR, 'a[data-wba-header-name="Cart"]')
    time.sleep(15)
    assert element.is_displayed()
