import pytest
from main.core.webdriverfactory import WebDriverFactory
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver_init(request, browser='chrome'):

    d = WebDriverFactory(browser=browser)
    driver = d.get_webdriver_instance()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()

    # if browser == 'chrome'
    # b = webdriver.Chrome(ChromeDriverManager().install())
    # b.implicitly_wait(10)
    # yield b
    # b.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", help="Enter browser type viz. chrome, firefox, egde")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
