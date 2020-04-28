from behave import *
from tests.configfile import EnvironmentSetup

use_step_matcher("re")


@given("User has been registered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    phone = EnvironmentSetup()
    phone.setUp()

@when("User lands on Coach's Corner page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("It is coming to 2nd step")
    # cctab = context.find_element_by_id("ui_tab_Coach's Corner")
    # cctab.click()
    # print(cctab.get_attribute('label'))



# def __init__(self, driver):
#     super().__init__(driver)
#     self.driver = driver
#     cctab = self.driver.find_element_by_id("ui_tab_Coach's Corner")
#     cctab.click()
#     print(cctab.get_attribute('label'))
#
