from pageobjects.landing_page import LandingPage
from pageobjects.home_page import HomePage
import traceback
from core.driver_init import get_browser
from behave.model_core import Status
import allure


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
    # print("Inside after step*****************************")
    # print(str(step.status))
    if step.status == Status.failed:
        # import pdb; pdb.set_trace()
        # pdb.post_mortem(step.exc_traceback)
        print("FAILED STEP NAME*******" + str(step.name))
        allure.attach(context.driver.take_screenshot(
        ), name="Error Screenshot", attachment_type=allure.attachment_type.PNG)

        trc = u"".join(traceback.format_tb(step.exc_traceback))
        print("FAILED ERROR TRACE*******" + str(trc))


# def after_scenario(context, scenario):
#     if scenario.status == Status.failed:
#         print(context.config.userdata['reporter'])
#         if context.config.userdata['reporter'] == 'allure':
#             print("Inside screenshot*****************")
#             allure.attach(context.driver.get_screenshot_as_png(
#             ), name="Error Screenshot", attachment_type=allure.attachment_type.PNG)


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
