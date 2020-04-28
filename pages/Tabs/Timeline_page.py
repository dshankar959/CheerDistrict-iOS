import time
from base.selenium_driver import SeleniumDriver
from appium.webdriver.common.touch_action import TouchAction
from utilities.scroll_recent_post import Scrolling
import utilities.custom_logger as cl
import logging
from pages.locators import Locator
import pytest

class TimelinePage(Locator, SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Method to performance action on the elements

    def clickViewAll(self):
        #self.getViewAll().click()
        self.elementClick(self._ViewAll, locatorType="xpath")

    def clickLike(self):
        #self.getLike().click()
        self.elementClick(self._like, locatorType="xpath")

    def clickCloseButton(self):
        #self.getClose().click()
        self.elementClick(self._close, locatorType="xpath")

    @pytest.mark.run(order=1)
    def VerifyViewAll(self):
        self.clickViewAll()
        time.sleep(2)
        self.clickLike()
        time.sleep(2)
        self.clickCloseButton()


