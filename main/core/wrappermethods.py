from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities import json_util


class WrapperMethods(object):

    __TIMEOUT = 10

    def __init__(self, driver):
        super(WrapperMethods, self).__init__()
        self.driver_wait = WebDriverWait(driver, WrapperMethods.__TIMEOUT)
        self._driver = driver

    def open(self):
        self._driver.get(json_util.get_value('base_url'))

    def maximize(self):
        self._driver.maximize_window()

    def close(self):
        self._driver.quit()

    def find_by_xpath(self, xpath):
        return self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def find_by_name(self, name):
        return self._driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def find_by_id(self, id):
        return self._driver_wait.until(EC.visibility_of_element_located((By.ID, id)))
