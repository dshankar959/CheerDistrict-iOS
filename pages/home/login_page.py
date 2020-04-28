import time
import utilities.custom_logger as cl
import logging
from pages.locators import Locator

class LoginPage(Locator):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

        #Locators
        # self._signin_button = "ui_sign_in"
        # self._toggle_button = "ui_toggle_button"
        # self._enter_phonenumber = "ui_input_text"
        # self._next_button = "ui_next_button"
        # self._enter_otp = "ui_input_text"
        # #Locator for email signin
        # self._enter_email = "ui_input_text"
        # self._successlogin = "ui_tab_Timeline"
        # self._failurelogin = "//XCUIElementTypeStaticText[@name='Please enter a valid email address.']"


    def getSignInButton(self):
        return self.driver.find_element_by_accessibility_id(self._signin_button)

    def getSelectPhoneButton(self):
        return self.driver.find_element_by_accessibility_id(self._toggle_button)

    def getEnterPhoneNumber(self):
        return self.driver.find_element_by_accessibility_id(self._enter_phonenumber)

    def getSelectNextButton(self):
        return self.driver.find_element_by_accessibility_id(self._next_button)

    def getEnterOtp(self):
        return self.driver.find_element_by_accessibility_id(self._enter_otp)

    def getDismissAlert(self):
        return self.driver.switch_to.alert.dismiss()

        #method for email button

    def getEnterEmail(self):
        return self.driver.find_element_by_accessibility_id(self._enter_email)

    def getSuccesslogin(self):
        tabname= self.driver.find_element_by_accessibility_id(self._successlogin)
        print(tabname.get_attribute("label"))
        return (tabname)

    def getFailurelogin(self):
        return self.driver.find_element_by_xpath(self._failurelogin)


    # Method to performance action on the elements

    def clickSignLink(self):
        # import pdb; pdb.set_trace()
        self.getSignInButton().click()

    def clickPhonebutton(self):
        self.getSelectPhoneButton().click()

    def EnterPhoneNumber(self, phonenumber):
        self.getEnterPhoneNumber().send_keys(phonenumber)

    # def EnterEmail(self, email):
    #     self.getEnterEmail().send_keys(email)

    def clickNextButton(self):
        self.getSelectNextButton().click()

    def Enterotp(self, key):
        self.getEnterOtp().send_keys(key)

    def DismissAlert(self):
        self.getDismissAlert()

    def VerifyLoginSuccess(self):
        result = self.getSuccesslogin()
        return result


    def validlogin(self, phonenumber, key):

        self.clickSignLink()
        time.sleep(2)
        self.clickPhonebutton()
        time.sleep(2)
        self.EnterPhoneNumber(phonenumber)
        time.sleep(2)
        self.clickNextButton()
        time.sleep(2)
        self.Enterotp(key)
        time.sleep(5)
        self.DismissAlert()
        self.VerifyLoginSuccess()

    def invalidlogin(self, phonenumber="", key=""):

        self.clickSignLink()
        time.sleep(2)
        self.clickPhonebutton()
        time.sleep(2)
        self.EnterPhoneNumber(phonenumber)
        time.sleep(2)
        self.clickNextButton()


    def VerifyLoginFailure(self):
        errormessage = self.driver.find_element_by_xpath(self._failurelogin).get_attribute("name")
        print(errormessage)
        if (errormessage == "Please enter a valid email address."):
            self.driver.quit()
        else:
            print("Login success")
        result = self.getFailurelogin()
        return result

