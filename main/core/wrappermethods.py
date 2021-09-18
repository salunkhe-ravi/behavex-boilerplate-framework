from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.utilities.json_util import JsonUtils as JSONUtils
from traceback import print_stack


class WrapperMethods(object):

    __TIMEOUT = 10

    def __init__(self, driver):
        super(WrapperMethods, self).__init__()
        self.driver_wait = WebDriverWait(driver, WrapperMethods.__TIMEOUT)
        self._driver = driver

    def open(self):
        self._driver.get(JSONUtils.get_value('base_url'))

    def maximize(self):
        self._driver.maximize_window()

    def quit(self):
        self._driver.quit()

    def find_by_xpath(self, xpath):
        return self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find_by_name(self, name):
        return self._driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def find_by_id(self, id):
        return self._driver_wait.until(EC.visibility_of_element_located((By.ID, id)))

    def click_by_id(self, id):
        try:
            element = self.find_by_id(id=id)
            element.click()
        except:
            print_stack()

    def click_by_name(self, name):
        try:
            element = self.find_by_name(name=name)
            element.click()
        except:
            print_stack()

    def click_by_xpath(self, xpath):
        try:
            element = self.find_by_xpath(xpath=xpath)
            element.click()
        except:
            print_stack()

    def enter_text_by_id(self, id, text):
        try:
            element = self.find_by_id(id=id)
            element.send_keys(text)
        except:
            print_stack()

    def enter_text_by_name(self, name, text):
        try:
            element = self.find_by_name(name=name)
            element.send_keys(text)
        except:
            print_stack()

    def enter_text_by_xpath(self, xpath, text):
        try:
            element = self.find_by_xpath(xpath=xpath)
            element.send_keys(text)
        except:
            print_stack()
