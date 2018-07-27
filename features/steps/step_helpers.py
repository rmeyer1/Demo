from __future__ import print_function


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import LONG_WAIT


def wait_until_element_is_clickable_by_id(context, element):

    try:
        WebDriverWait(context.driver, LONG_WAIT).until(EC.element_to_be_clickable((By.ID, element)))

    except:
        print('could not locate element %s' % (element))


def wait_until_element_is_clickable_by_class_name(context, element):

    try:
        WebDriverWait(context.driver, LONG_WAIT).until(EC.element_to_be_clickable((By.CLASS_NAME, element)))

    except:
        print('could not locate element %s' % (element))


def select_email(context, name, element):
    try:
        emails = context.driver.find_elements_by_class_name(element)
        assert emails

        # assuming we are always clicking
        # the email passed in from name parameter
        for email in emails:
            if email.text == name:
                email.click()
                break

    except:
        print('Could not locate the email with name %s' % (name))


def validate_button(context, element):

    try:

        button = context.driver.find_element_by_class_name(element)
        assert button
        button.click()

    except:
        print("Could not validate button.  Please check locator.")


def activate_virtru_plugin(context, my_email):

    try:

        validate_button(context, 'CToWUd')

        # At this point 2 windows are in view
        # I am switching the active window
        # to the newest tab to complete google auth
        active_windows = context.driver.window_handles
        context.driver.switch_to.window(active_windows[1])

        wait_until_element_is_clickable_by_class_name(context, "btn-container")

        select_email(context, my_email, "btn-container")

        validate_button(context, 'oauthButton')

    except:
        print("Could not activate Virtu Plugin using %s.  Please ensure email parameter is correct & check your locators." % (my_email))


def validate_encrypted_email(context, email_subject, body_text):

    wait_until_element_is_clickable_by_class_name(context, 'subject')

    current_subject = context.driver.find_element_by_class_name('subject')
    assert current_subject
    current_body = context.driver.find_element_by_class_name('tdf-body')
    assert current_body

    assert current_subject.text == email_subject
    assert current_body.text == body_text

