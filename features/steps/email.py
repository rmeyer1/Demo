from __future__ import print_function, unicode_literals

from behave import step


from features.steps import step_helpers


@step("Locate and Validate Email")
def step_impl(context):

    step_helpers.select_email(context, "Rob Meyer", "yW")

    step_helpers.activate_virtru_plugin(context, "rob.meyer.automationtests@gmail.com")

    step_helpers.validate_encrypted_email(context, "test", "this is a UI test")


