import unittest
import datetime
from appium import webdriver
from pages.home.login_page import LoginPage
import pytest

class EnvironmentSetup(unittest.TestCase):


    def setUp(self) -> object:
        print("Running one time setUp at: "+str(datetime.datetime.now()))
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'iOS'
        self.desired_caps['platformVersion'] = '12.1'
        self.desired_caps['automationName'] = 'xcuitest'
        self.desired_caps['deviceName'] = 'iPhone Simulator'
        self.desired_caps['newCommandTimeout'] = '6000'
        #self.desired_caps['autoDismissAlerts'] = 'true'
        #self.desired_caps['permission', 'microphone'] = 'NO'
        self.desired_caps['app'] = '//Users//qa//Desktop//CheerDistrict.app'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(6000)

        lp = LoginPage(self.driver)
        lp.validlogin("6471231231", "022455")

    def tearDown(self):
        if (self.driver != None):
            print("-------------------------------------------")
            print("Run Completed at : " + str(datetime.datetime.now()))
            self.driver.quit()


# if name == 'main':
#     unittest.main()