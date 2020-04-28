import time
from base.selenium_driver import SeleniumDriver
from appium.webdriver.common.touch_action import TouchAction
from utilities.scroll_recent_post import Scrolling
import utilities.custom_logger as cl
import logging
from pages.locators import Locator
import pytest

class CreatePost(Locator, SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Method to performance action on the elements

    def clickCreatePost(self):
        self.elementClick(self._write_a_post, locatorType="id")

    # def tagfriend(self):
    #     self.elementClick(self._tagfriend, locatorType="id")

    def clickPhotoButton(self):
        self.elementClick(self._photo_button, locatorType="id")

    def clickPhotoLibrary(self):
        self.elementClick(self._photo_library, locatorType="id")
        touch = TouchAction(self.driver)
        touch.tap(element=None, x=8, y=656, count=1).release().perform()
        time.sleep(5)

        #TouchAction(self.driver).tap(elment=None, x=180, y=685, count=2).perform()
        #TouchAction.tap(self.driver, element=None, x=191, y=676, count=1).perform()

    def clickCameraRoll(self):
        self.elementClick(self._camera_roll, locatorType="id")

    def selectPhoto(self):
        self.elementClick(self._photo_gridview, locatorType='id')

    def postPhoto(self):
        self.elementClick(self._post_button, locatorType='id')

    #click on profile pic to see the post in personal timeline
    def clickProfilepic(self):
        self.elementClick(self._profile_pic_button, locatorType='xpath')


    @pytest.mark.run(order=1)
    def VerifyCreatePost(self):
        self.clickCreatePost()
        time.sleep(2)
        self.clickPhotoButton()
        time.sleep(2)
        self.clickPhotoLibrary()
        time.sleep(3)
        self.clickCameraRoll()
        time.sleep(3)
        self.selectPhoto()
        time.sleep(3)
        self.postPhoto()
        time.sleep(3)
        self.clickProfilepic()
        time.sleep(3)


