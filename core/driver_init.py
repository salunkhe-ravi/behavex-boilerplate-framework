from selenium import webdriver
from core.web_wrapper_functions import WebWrapperFunctions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def get_browser(browser):
    """
    Returns the instance of the browser provided

    Keyword arguments:
    browser -- Name of the browser to invoke
    Return: instance of the browser driver
    """
    if browser == "chrome":
        return WebWrapperFunctions(webdriver.Chrome(ChromeDriverManager().install()))
    elif browser == 'firefox':
        return WebWrapperFunctions(webdriver.Firefox(executable_path=GeckoDriverManager().install()))
    elif browser == 'edge':
        return WebWrapperFunctions(webdriver.Edge(EdgeChromiumDriverManager().install()))
    else:
        raise Exception('No valid browser argument provided, pls verify')
