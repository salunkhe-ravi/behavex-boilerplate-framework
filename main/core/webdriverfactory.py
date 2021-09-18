
from selenium import webdriver
from main.core.wrappermethods import WrapperMethods
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser

    def get_webdriver_instance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome(ChromeDriverManager().install())
            WrapperMethods(driver)
        else:
            driver = webdriver.Firefox()

        # Setting Driver Implicit Time out for An Element
        # driver.implicitly_wait(3)
        # Maximize the window
        WrapperMethods.maximize(self)
        # Loading browser with App URL
        WrapperMethods.open(self)
        return WrapperMethods(driver)
