from pages.home.login_page import LoginPage
import pytest
import time
from tests.configfile import EnvironmentSetup
from pages.Tabs.menu_page import MenuPage
from utilities.scroll_recent_post import Scrolling
from utilities.teststatus import TestStatus
from utilities.screenshot import Screenshottest
import unittest

class MenuTabTests(EnvironmentSetup):


    @pytest.mark.run(order=1)
    def test_menutab(self):
        self.mn = MenuPage(self.driver)
        # self.mn.VerifyMenutab()
        # self.mn.VerifycreateOrg()
        # self.mn.VerifyProfilePrivacy()
        # tc = Scrolling(self.driver)
        # tc.scroll_to_element(self)
        # self.mn.VerifyTips()
        # sc = Screenshottest(self.driver)
        # sc.screenShot(self)


        ##  reated this for screenshot taking when tests fails, but did not work needs to fix TestStatus file
        self.ts = TestStatus(self.driver)
        result1 = self.mn.VerifyMenutab()
        self.ts.mark(result1, "Menu tab verification")

        result2 = self.mn.VerifycreateOrg()
        self.ts.mark(result2, "Create Organization Verification")
        tc = Scrolling(self.driver)
        tc.scroll_to_element(self)

        result3 = self.mn.VerifyProfilePrivacy()
        self.ts.mark(result3, "Profile Privacy Verification")

        result4 = self.mn.VerifyTips()
        self.ts.mark(result4, "Tips Verification")








