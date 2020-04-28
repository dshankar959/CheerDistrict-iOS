import time
from base.selenium_driver import SeleniumDriver
from appium.webdriver.common.touch_action import TouchAction
from utilities.scroll_to_view_allworkouts import Scrolling
import utilities.custom_logger as cl
import logging
from pages.locators import Locator
import pytest

class Training(Locator, SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Method to performance action on the elements

    def clickTrainingTab(self):
        self.elementClick(self._switch_training_tab, locatorType="id")
        time.sleep(5)

    #count number of workouts available

    def countworkouts(self):
        parent_elements= self.driver.find_elements_by_class_name("XCUIElementTypeCell")
        total_parent_elements = len(parent_elements)
        print("Total Parent elements= "+str(total_parent_elements))
        parent = self.driver.find_element_by_class_name("XCUIElementTypeCell")

        workoutsList = self.driver.find_elements_by_xpath("//XCUIElementTypeCell/XCUIElementTypeButton")
        total_workouts = len(workoutsList)
        print("Total workouts in this week: " +str(total_workouts))

        completed_workouts = self.driver.find_elements_by_xpath("//XCUIElementTypeCell/XCUIElementTypeStaticText")
        total_completed_workouts = len(completed_workouts)
        print("Total completed workouts= " +str(total_completed_workouts))
        time.sleep(3)
        ### Select the workout which is not completed #####
        for i in range(total_completed_workouts):
            value = completed_workouts[i].get_attribute('value')
            print(value)
            if value == '' or value is None:
                time.sleep(3)
                completed_workouts[i - 1].click()
                continue_button = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='CONTINUE TRAINING']")
                continue_button.click()
                # self.elementClick(self._continue_training, locatorType='id')
                start_button = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='START']")
                # if start_button.is_displayed():
                #     print("Start button is available")

                for i in range(10):
                    start_button.click()
                    complete_button = self.driver.find_element_by_id("COMPLETE")
                    if complete_button.is_displayed():
                       complete_button.click()
                    else:
                        duration = self.driver.find_element_by_id("ui_timer_label")
                        wait_time = duration.get_attribute('value')
                        print(wait_time)
                        time.sleep(wait_time)
            else:
                print("Workout can't be selected")


    @pytest.mark.run(order=1)
    def VerifyTrainingTab(self):
        self.clickTrainingTab()
        time.sleep(10)
        self.countworkouts()
        time.sleep(30)







