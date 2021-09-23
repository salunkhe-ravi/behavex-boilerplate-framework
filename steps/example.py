# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step


@given('user navigates to the site')
def step_impl(context):
    context.homepage.navigate_to_app(context)


@when('user enters "{data}" in the search box')
def step_impl(context, data):
    context.homepage.enter_text_to_search(context, data)


@when('user clicks on the search button')
def step_impl(context):
    context.homepage.click_search_button(context)


@then('user validates "{data}" on landing page')
def step_impl(context, data):
    context.landingpage.verify_display_name(context, data)


@then('user validates "{data}" in header section')
def step_impl(context, data):
    context.landingpage.verify_header_name(context, data)
