import os.path
import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

URL_THE_INTERNET = 'https://the-internet.herokuapp.com/'


@allure.suite("Selenium_advanced")
@allure.sub_suite("Clicks")
class TestClicks:
    @allure.title("Click_normal")
    def test_click(self, driver):
        url = f'{URL_THE_INTERNET}/checkboxes'
        driver.get(url)
        element = driver.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]')
        element.click()
        assert element.is_selected()

    @allure.title("Click_jc")
    def test_click_jc(self, driver):
        url = f'{URL_THE_INTERNET}/hovers'
        driver.get(url)
        element = driver.find_element(By.XPATH, '//*/a[@href="/users/3"]')
        driver.execute_script("arguments[0].click()", element)
        time.sleep(5)
        assert driver.title != 'The Internet'

    @allure.title("Click_keyboard")
    def test_click_keyboard(self, driver):
        url = f'{URL_THE_INTERNET}/key_presses'
        driver.get(url)
        action: ActionChains = ActionChains(driver)
        action.key_down(Keys.ENTER).perform()
        element = driver.find_element(By.XPATH, '//*[@id="result"]')
        assert element.text == 'You entered: ENTER'

    @allure.title("Click_mouse")
    def test_click_mouse(self, driver):
        url = f'{URL_THE_INTERNET}/context_menu'
        driver.get(url)
        element = driver.find_element(By.XPATH, '//*[@id="hot-spot"]')
        action: ActionChains = ActionChains(driver)
        action.context_click(element).perform()
        alert = driver.switch_to.alert
        assert alert.text == 'You selected a context menu'
        alert.accept()

@allure.suite("Selenium_advanced")
@allure.sub_suite("Text")
class TestText:
    @allure.title("Text_add")
    def test_text_add(self, driver):
        url = f'{URL_THE_INTERNET}/inputs'
        driver.get(url)
        element = driver.find_element(By.XPATH, '//*[@type="number"]')
        element.send_keys('76')
        assert element.get_attribute("value") == '76'

    @allure.title("Text_clear")
    def test_text_clear(self, driver):
        url = f'{URL_THE_INTERNET}/inputs'
        driver.get(url)
        element = driver.find_element(By.XPATH, '//*[@type="number"]')
        element.clear()
        assert element.get_attribute("value") == ''

@allure.suite("Selenium_advanced")
@allure.sub_suite("Alert")
class TestAlert:
    @allure.title("Simple_alert_accept")
    def test_simple_alert(self, driver):
        url = f'{URL_THE_INTERNET}/javascript_alerts'
        driver.get(url)
        button = driver.find_element(By.XPATH, '//*[1]/button')
        button.click()
        alert = driver.switch_to.alert
        assert alert.text == 'I am a JS Alert'
        alert.accept()
        result = driver.find_element(By.XPATH, '//*[@id="result"]')
        assert result.text == "You successfully clicked an alert"

    @allure.title("Confirmation_alert_accept")
    def test_confirmation_alert_accept(self, driver):
        url = f'{URL_THE_INTERNET}/javascript_alerts'
        driver.get(url)
        button = driver.find_element(By.XPATH, '//*[2]/button')
        button.click()
        alert = driver.switch_to.alert
        assert alert.text == 'I am a JS Confirm'
        alert.accept()
        result = driver.find_element(By.XPATH, '//*[@id="result"]')
        assert result.text == "You clicked: Ok"

    @allure.title("Confirmation_alert_dismiss")
    def test_confirmation_alert_dismiss(self, driver):
        url = f'{URL_THE_INTERNET}/javascript_alerts'
        driver.get(url)
        button = driver.find_element(By.XPATH, '//*[2]/button')
        button.click()
        alert = driver.switch_to.alert
        assert alert.text == 'I am a JS Confirm'
        alert.dismiss()
        result = driver.find_element(By.XPATH, '//*[@id="result"]')
        assert result.text == 'You clicked: Cancel'

    @allure.title("Prompt_alert_accept")
    def test_prompt_alert_accept(self, driver):
        url = f'{URL_THE_INTERNET}/javascript_alerts'
        driver.get(url)
        button = driver.find_element(By.XPATH, '//*[3]/button')
        button.click()
        alert = driver.switch_to.alert
        assert alert.text == 'I am a JS prompt'
        alert.send_keys('Answer')
        alert.accept()
        result = driver.find_element(By.XPATH, '//*[@id="result"]')
        assert result.text == 'You entered: Answer'

    @allure.title("Prompt_alert_dismiss")
    def test_prompt_alert_dismiss(self, driver):
        url = f'{URL_THE_INTERNET}/javascript_alerts'
        driver.get(url)
        button = driver.find_element(By.XPATH, '//*[3]/button')
        button.click()
        alert = driver.switch_to.alert
        assert alert.text == 'I am a JS prompt'
        alert.dismiss()
        result = driver.find_element(By.XPATH, '//*[@id="result"]')
        assert result.text == 'You entered: null'


@allure.suite("Selenium_advanced")
@allure.sub_suite("Working_with_tabs")
@allure.title("Tabs")
def test_working_with_tabs(driver):
    url = f'{URL_THE_INTERNET}/windows'
    driver.get(url)
    link = driver.find_element(By.XPATH, '//a[@href="/windows/new"]')
    link.click()
    main_window = driver.current_window_handle
    new_window = [window for window in driver.window_handles if window != main_window][0]
    driver.switch_to.window(new_window)
    time.sleep(3)
    assert driver.title == 'New Window'


@allure.suite("Selenium_advanced")
@allure.sub_suite("IFrame")
@allure.title("IFrame")
def test_switch_to_frame(driver):
    url = f'{URL_THE_INTERNET}/iframe'
    driver.get(url)
    element = driver.find_element(By.XPATH, '//iframe')
    driver.switch_to.frame(element)
    content = driver.find_element(By.XPATH, '//p')
    assert content.text == 'Your content goes here.'
    driver.switch_to.default_content()


@allure.suite("Selenium_advanced")
@allure.sub_suite("Files")
class TestFiles:
    @allure.title("File_upload")
    def test_file_upload(self, driver):
        url = f'{URL_THE_INTERNET}/upload'
        driver.get(url)
        file_upload = driver.find_element(By.XPATH, '//*[@id="file-upload"]')
        file_path = os.path.abspath('/Users/itsta/Desktop/test/upload.txt')
        file_upload.send_keys(file_path)
        file_submit = driver.find_element(By.XPATH, '//*[@id="file-submit"]')
        file_submit.click()
        message = driver.find_element(By.XPATH, '//*/h3')
        file_name = driver.find_element(By.XPATH, '//*[@id="uploaded-files"]')
        assert message.text == 'File Uploaded!'
        assert file_name.text == 'upload.txt'

    @allure.title("File_download")
    def test_file_download(self, driver):
        url = f'{URL_THE_INTERNET}/download'
        driver.get(url)
        driver.implicitly_wait(7)
        download_link = driver.find_element(By.XPATH, '//*/a[contains(@href,"upload.txt")]')
        download_link.click()
        download = os.path.abspath('/Users/itsta/Downloads')
        expected_file = os.path.join(download, "upload.txt")
        assert os.path.exists(expected_file)

