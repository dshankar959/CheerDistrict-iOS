import time
from base.selenium_driver import SeleniumDriver
from appium.webdriver.common.touch_action import TouchAction
from utilities.scroll_recent_post import Scrolling
import utilities.custom_logger as cl
import logging
from pages.locators import Locator
import pytest

class MenuPage(Locator, SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Method to performance action on the elements

    def clickMenuTab(self):
        self.elementClick(self._menu_tab, locatorType="id")

    def clickSelectProfile(self):
        self.elementClick(self._profile_detail, locatorType="id")

    def clickEditButton(self):
        self.elementClick(self._edit_button, locatorType="id")

    def clickSaveButton(self):
        self.elementClick(self._save_button, locatorType="id")

    def clickBackButton(self):
        self.elementClick(self._back_button, locatorType="id")

    def clickOrganization(self):
        self.elementClick(self._organization, locatorType="id")

    def clickCreateOrgbutton(self):
        self.elementClick(self._create_org, locatorType="id")

    def enterOrgName(self, orgname):
        self.sendKeys(orgname, self._enter_orgname, locatorType="xpath")

    def clickProfilePrivacy(self):
        self.elementClick(self._profile_privacy, locatorType="id")

    def clickPrivacyLevel1(self):
        self.elementClick(self._privacy_level1, locatorType="id")

    def clickPrivacyLevel2(self):
        self.elementClick(self._privacy_level2, locatorType="id")

    def clickPrivacyLevel3(self):
        self.elementClick(self._privacy_level3, locatorType="id")

    def clickAllowFriendreq(self):
        self.elementClick(self._allow_friendreq, locatorType="xpath")

    def clickMyTraining(self):
        self.elementClick(self._my_Training_Act, locatorType="id")

    def clickOkDialog(self):
        self.elementClick(self._ok_dialog, locatorType="name")

    def scrolltillsignout(self):
        # touch = TouchAction(self.driver)
        # touch.press(x=148, y=546).move_to(x=148, y=260).release().perform()
        self.elementClick(self._signout, locatorType="id")

    def clickTips(self):
        self.elementClick(self._tips1, locatorType="id")

    def clickContactUs(self):
        self.elementClick(self._contactus, locatorType="id")

    def clickPrivacyPolicy(self):
        self.elementClick(self._privacy_policy, locatorType="id")

    def clickCancelButton(self):
        self.elementClick(self._cancel_button, locatorType="id")

    @pytest.mark.run(order=1)
    def VerifyMenutab(self):
        self.clickMenuTab()
        time.sleep(2)
        self.clickSelectProfile()
        time.sleep(2)
        self.clickEditButton()
        time.sleep(2)
        self.clickSaveButton()
        time.sleep(2)
        self.clickBackButton()
        time.sleep(3)


    @pytest.mark.run(order=2)
    def VerifycreateOrg(self, orgname="August_20_Test"):
        self.clickMenuTab()
        time.sleep(2)
        self.clickOrganization()
        time.sleep(2)
        self.clickCreateOrgbutton()
        time.sleep(2)
        self.enterOrgName(orgname)
        time.sleep(3)
        self.clickSaveButton()
        time.sleep(2)
        self.clickBackButton()

    @pytest.mark.run(order=3)
    def VerifyProfilePrivacy(self):
        self.clickProfilePrivacy()
        time.sleep(2)
        self.clickPrivacyLevel1()
        time.sleep(2)
        self.clickPrivacyLevel2()
        time.sleep(2)
        self.clickPrivacyLevel3()
        time.sleep(2)
        self.clickAllowFriendreq()
        time.sleep(2)
        self.clickAllowFriendreq()
        time.sleep(2)
        self.clickBackButton()
        time.sleep(2)
        # self.clickMyTraining()
        # time.sleep(2)
        # self.clickOkDialog()
        # time.sleep(3)

    @pytest.mark.run(order=4)
    def VerifyTips(self):
        self.clickTips()
        time.sleep(2)
        self.clickBackButton()
        time.sleep(2)

        self.clickContactUs()
        time.sleep(2)
        self.clickBackButton()
        # time.sleep(2)
        # self.clickPrivacyPolicy()
        # time.sleep(2)
        # self.clickCancelButton()













