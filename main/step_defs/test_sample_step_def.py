import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Constants

DUCKDUCKGO_HOME = 'https://duckduckgo.com/'

# Scenarios

scenarios('Feature1.feature', 'Feature2.feature')

# Fixtures

# Given Steps


@given('the DuckDuckGo home page is displayed')
def ddg_home(driver):
    driver.get(DUCKDUCKGO_HOME)
    print("step 1 executed")

# When Steps


@when(parsers.parse('the user searches for "{phrase}"'))
def search_phrase(driver, phrase):
    search_input = driver.find_element_by_id('search_form_input_homepage')
    search_input.send_keys(phrase + Keys.RETURN)

# Then Steps


@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(driver, phrase):
    # Check search result list
    # (A more comprehensive test would check results for matching phrases)
    # (Check the list before the search phrase for correct implicit waiting)
    links_div = driver.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    # Check search phrase
    search_input = driver.find_element_by_id('search_form_input')
    assert search_input.get_attribute('value') == phrase
