from behave import *
from tests.configfile import EnvironmentSetup

use_step_matcher("re")


@given("User has been signedup")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    phone = EnvironmentSetup()
    phone.setUp()

@when("User sign in back land on cc page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("This is second step")