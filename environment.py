from pageobjects.landing_page import LandingPage
from pageobjects.home_page import HomePage
from selenium import webdriver
from traceback import print_stack
from core.driver_init import get_browser
from behave.model_core import Status


def before_all(context):
    try:
        if context.config.userdata['browser'].lower() == 'chrome':
            driver = get_browser('chrome')
            context.driver = driver
        elif context.config.userdata['browser'].lower() == 'firefox':
            driver = get_browser('firefox')
            context.driver = driver
        elif context.config.userdata['browser'].lower() == 'edge':
            driver = get_browser('edge')
            context.driver = driver
    except:
        print("*********Non-browser test*********")


def after_all(context):
    context.driver.close()


def after_step(context, step):
    print("Inside after step*****************************")
    print(str(step.status))
    if step.status == Status.failed:
        print("FAILED*******" + str(step.name))
        print("FAILED*******" + str(step.error_message))

def after_scenario(context, scenario):
    print("after scenario*********" + "")

def before_scenario(context, scenario):
    context.homepage = HomePage()
    context.landingpage = LandingPage()

# def before_scenario(context, scenario):
#     print("This is before scenario")
#     if 'web' in context.tags:
#         context.browser = webdriver.Firefox()
#         context.browser.implicitly_wait(10)


# def after_scenario(context, scenario):
#     print("This is after scenario")
#     if 'web' in context.tags:
#         context.browser.quit()
