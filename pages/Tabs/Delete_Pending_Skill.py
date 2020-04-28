import time
from base.selenium_driver import SeleniumDriver
from appium.webdriver.common.touch_action import TouchAction
from utilities.scroll_recent_post import Scrolling
import utilities.custom_logger as cl
import logging
from pages.locators import Locator
import pytest
from pages.Tabs import menu_page


class DeletePendingSkill(Locator, SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Method to performance action on the elements


    def clickProfilepic(self):
        self.elementClick(self._profile_pic_button, locatorType='xpath')

    def clickEdit(self):
        self.elementClick(self._edit, locatorType='id')

    def countSkills(self):
        skills = self.driver.find_elements_by_xpath(self._skills)
        total_skills = len(skills)
        print("Total skill: " + str(total_skills))
        skills[3].click()

    def clickPendingState(self):
        self.elementClick(self._pending, locatorType='id')

    @pytest.mark.run(result=1)
    def VerifyDeletePendingSkill(self):
        self.clickProfilepic()
        time.sleep(3)
        self.clickEdit()
        time.sleep(5)
        self.clickPendingState()
        time.sleep(3)
        self.countSkills()
        time.sleep(3)





