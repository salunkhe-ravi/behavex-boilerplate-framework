from selenium import webdriver
from core.wrapper_functions import WrapperFunctions
from webdriver_manager.chrome import ChromeDriverManager

def get_browser(browser):
    if browser == "chrome":
        return WrapperFunctions(webdriver.Chrome(ChromeDriverManager().install()))
    else:
        raise Exception('No valid browser provided')    
