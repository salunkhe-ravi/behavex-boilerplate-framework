# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step
from utils.util import get_profiles_value

@given('user navigates to the site')
def step_impl(context):
    context.wrapper.open(get_profiles_value(context,'app_url'))


@when('user enters "{data}" in the search box')
def step_impl(context, data):
    context.wrapper.enter_text_by_id('searchInput',data)


@when('user clicks on the search button')
def step_impl(context):
    context.wrapper.click_element_by_xpath("//i[@class='sprite svg-search-icon']")


@then('user lands on search page')
def step_impl(context):
    pass