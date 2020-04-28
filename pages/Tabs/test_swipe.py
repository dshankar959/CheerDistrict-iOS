import time
from base.selenium_driver import SeleniumDriver
from appium.webdriver.common.touch_action import TouchAction
from utilities.scroll_recent_post import Scrolling
from pages.locators import Locator
import utilities.custom_logger as cl
import logging
from pages.locators import Locator
import pytest

class Swipe(Locator, SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def Swipeup(self):
        for i in range(5):
            touch = TouchAction(self.driver)
            touch.press(x=210, y=571).wait(500).move_to(x=210, y=339).release().perform()
            time.sleep(5)

    @pytest.mark.run(order=1)
    def VerifySwipe(self):
        self.Swipeup()

