import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

URL_WB = 'https://www.wildberries.by/'


@allure.suite("Locators")
@allure.sub_suite("XPATH")
@allure.title("Banner_is_present")
def test_xpath_banner_is_present(driver):
    driver.get(URL_WB)
    element = WebDriverWait(driver, 10).until(ec.visibility_of_element_located(
            (By.XPATH, '//*[contains(@class, "main-page__banner") and contains(@class, "banner")]')))
    assert element.is_displayed()

@allure.suite("Locators")
@allure.sub_suite("XPATH")
@allure.title("Currency_icon_is_present")
def test_xpath_currency_icon_is_present(driver):
    driver.get(URL_WB)
    element = driver.find_element(By.XPATH, '//*[@class="simple-menu__currency"]')
    time.sleep(10)
    assert element.is_displayed()

@allure.suite("Locators")
@allure.sub_suite("XPATH")
@allure.title("Navigator_menu_is_present")
def test_xpath_navigator_menu_is_present(driver):
    driver.get(URL_WB)
    element = driver.find_element(By.XPATH, '//button[contains(@class,"burger")]')
    assert element.is_displayed()

@allure.suite("Locators")
@allure.sub_suite("XPATH")
@allure.title("Search_field_is_present")
def test_xpath_search_field_is_present(driver):
    driver.get(URL_WB)
    element = driver.find_element(By.XPATH, '//*[@id="searchBlock"]')
    assert element.is_displayed()

@allure.suite("Locators")
@allure.sub_suite("XPATH")
@allure.title("Site_logo_is_present")
def test_xpath_site_logo_is_present(driver):
    driver.get(URL_WB)
    element = driver.find_element(By.XPATH, '//*[contains(@class,"nav-element__logo")]')
    assert element.is_displayed()

@allure.suite("Locators")
@allure.sub_suite("XPATH")
@allure.title("Basket_is_present")
def test_xpath_basket_is_present(driver):
    driver.get(URL_WB)
    element = driver.find_element(By.XPATH, '//*/a[@data-wba-header-name="Cart"]')
    assert element.is_displayed()
