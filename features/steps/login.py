from __future__ import print_function, unicode_literals

from behave import given, step

from settings import USERS
from features.steps import step_helpers


@given("the browser is open to GMAIL")
def step_impl(context):

    application_url = 'http://www.gmail.com'

    context.driver.get(application_url)


@step("the user is logged in as {user_type}")
def step_impl(context, user_type):
    user = USERS[user_type]

    login_form = context.driver.find_element_by_id("view_container")

    username_textbox = login_form.find_element_by_name("identifier")
    assert username_textbox
    username_textbox.send_keys(user["username"])

    next_button = context.driver.find_element_by_id('identifierNext')
    assert next_button
    next_button.click()

    step_helpers.wait_until_element_is_clickable_by_id(context, "password")

    password_textbox = login_form.find_element_by_name("password")
    assert password_textbox
    password_textbox.send_keys(user["password"])

    step_helpers.wait_until_element_is_clickable_by_id(context, 'passwordNext')

    final_submit = context.driver.find_element_by_id('passwordNext')
    assert final_submit
    final_submit.click()

    step_helpers.wait_until_element_is_clickable_by_id(context, "gbqfb")



