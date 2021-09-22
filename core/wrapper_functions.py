from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from traceback import print_stack


class WrapperFunctions(object):

    __TIMEOUT = 10

    def __init__(self, driver):
        super(WrapperFunctions, self).__init__()
        self._driver_wait = WebDriverWait(driver, WrapperFunctions.__TIMEOUT)
        self._driver = driver

    def open(self, url):
        self._driver.get(url)

    def maximize(self):
        self._driver.maximize_window()

    def close(self):
        self._driver.quit()

    def find_by_id(self, id):
        return self._driver_wait.until(EC.visibility_of_element_located((By.ID, id)))

    def find_by_name(self, name):
        return self._driver_wait.until(EC.visibility_of_element_located((By.NAME, name)))

    def find_by_xpath(self, xpath):
        return self._driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def enter_text_by_id(self, id, text):
        """enter text in the web element

        Args:
            id ([type]): provide the id of the element
            text ([type]): provide the text to be entered
        """
        self.find_by_id(id).send_keys(text)

    def enter_text_by_name(self, name, text):
        self.find_by_name(name).send_keys(text)

    def enter_text_by_xpath(self, xpath, text):
        self.find_by_xpath(xpath).send_keys(text)

    def click_element_by_id(self, id):
        self.find_by_id(id).click()

    def click_element_by_name(self, name):
        self.find_by_name(name).click()

    def click_element_by_xpath(self, xpath):
        self.find_by_xpath(xpath).click()
