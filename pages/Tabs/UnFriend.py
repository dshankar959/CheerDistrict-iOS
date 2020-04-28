import time
from base.selenium_driver import SeleniumDriver
from appium.webdriver.common.touch_action import TouchAction
from utilities.scroll_recent_post import Scrolling
import utilities.custom_logger as cl
import logging
from pages.locators import Locator
import pytest

class DeleteFriend(Locator, SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Method to performance action on the elements


    #click on profile pic to see the post in personal timeline
    def clickProfilepic(self):
        self.elementClick(self._profile_pic_button, locatorType='xpath')


    def clickSeeAll(self):
        # self.elementClick(self._seeAll, locatorType='xpath')
        touch = TouchAction(self.driver)
        #touch.tap(self, x=307, y=458, Duration=1).release().perform()
        touch.tap(element=None, x=307, y=458, count=1).release().perform()

    def countAllFriends(self):
        count_friends = self.driver.find_elements_by_xpath(self._friends_list)
        total_count_friends = len(count_friends)
        print("Total count of friends= " + str(total_count_friends))
        count_friends[1].click()
        self.elementClick(self._profile_right_bar, locatorType='id')
        time.sleep(3)
        self.elementClick(self._unfriend_button, locatorType='id')
        time.sleep(3)

        # self.driver.find_element_by_xpath("//XCUIElementTypeApplication[@name='Cheer District']/XCUIElementTypeWindow[1]/XCUIElementTypeOther[2]/XCUIElementTypeSheet/XCUIElementTypeOther/XCUIElementTypeOther[1]").click()
        alert = self.driver.switch_to.alert()
        alert.accept()


        ############## Using Java script executer ##################
        #self.driver.execute_script("target.frontMostApp().actionSheet().buttons()[1].tap()")
        #self.driver.execute_script("target.frontMostApp().actionSheet().collectionViews()[0].visibleCells()[0].tap()")

        ################# Using Touch Action ##################
        # touch = TouchAction(self.driver)
        # touch.tap(element=None, x=8, y=656, count=1).release().perform()
        # time.sleep(5)

        ############# Using uiautomation###############
        # sheet = self.driver.find_element_by_ios_uiautomation("UIATarget.localTarget().frontMostApp().actionSheet().elements()[1]").text
        # print("Sheet: " + sheet)

        ############## Using Java script executer ##################
        #self.driver.execute_script("UIATarget.localTarget().frontMostApp().actionSheet().elements()[1].tap()")
        #self.driver.execute_script("target.frontMostApp().actionSheet().collectionViews()[0].visibleCells()[0].tap()")

        ######### Using as alert message ##############
        #self.driver.switch_to_alert().accept()


    @pytest.mark.run(order=1)
    def VerifySelectProfile(self):
        self.clickProfilepic()
        time.sleep(2)

    @pytest.mark.run(order=2)
    def VerifySeeAllFriends(self):
        self.clickSeeAll()
        time.sleep(3)
        self.countAllFriends()
        time.sleep(3)





