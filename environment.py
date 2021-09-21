from selenium import webdriver
from traceback import print_stack
from core.driver_init import get_browser


def before_all(context):
    try:
        if context.config.userdata['browser'].lower() == 'chrome':
            driver = get_browser('chrome')
            context.wrapper = driver
        elif context.config.userdata['browser'].lower() == 'firefox':
            driver = get_browser('firefox')
            context.wrapper = driver
        elif context.config.userdata['browser'].lower() == 'edge':
            driver = get_browser('edge')
            context.wrapper = driver
    except:
        print("*********No browser argument(-D browser=?) provided defaulting to chrome*********")
        driver = get_browser('chrome')
        context.wrapper = driver


def after_all(context):
    context.wrapper.close()


def before_scenario(context, scenario):
    print("This is before scenario")
    if 'web' in context.tags:
        context.browser = webdriver.Firefox()
        context.browser.implicitly_wait(10)


def after_scenario(context, scenario):
    print("This is after scenario")
    if 'web' in context.tags:
        context.browser.quit()
