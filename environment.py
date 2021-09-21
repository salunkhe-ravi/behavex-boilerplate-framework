from selenium import webdriver

from core.driver_init import get_browser


def before_all(context):
    driver = get_browser(context.config.userdata['browser'])
    context.wrapper = driver

    # Local Chrome WebDriver
    # if context.browser == "chrome":
    #   context.driver = webdriver.Chrome()


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
