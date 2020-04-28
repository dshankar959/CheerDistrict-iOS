import time
import datetime
from base.selenium_driver import SeleniumDriver
from appium.webdriver.common.touch_action import TouchAction
from utilities.scroll_to_view_allworkouts import Scrolling
import utilities.custom_logger as cl
import logging
from pages.locators import Locator
import pytest


class TrainingProgress(Locator, SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Method to performance action on the elements

    def clickTrainingTabTest(self):
        self.elementClick(self._switch_training_tab, locatorType="id")
        time.sleep(5)

    #count number of workouts available

    def countworkoutsTest(self):
        ### Getting Collapse view week ####
        first_week = self.driver.find_element_by_xpath("(//XCUIElementTypeOther[@name='ui_section_week'])[1]")
        first_week.click()
        ### Counting Total number of weeks ####
        number_weeks= self.driver.find_elements_by_id("ui_section_week")
        total_weeks = len(number_weeks)
        print("Total weeks= "+str(total_weeks))

        ### Checking each week activity ####

        for i in range(total_weeks):
            number_weeks[i].click()

            ### Getting total number of workouts on particular week ##
            workoutsList = self.driver.find_elements_by_xpath("//XCUIElementTypeCell/XCUIElementTypeButton")
            total_workouts = len(workoutsList)
            print("Total workouts in this week: " + str(total_workouts))

            ## Getting completed workouts on that particular week ##
            completed_workouts = self.driver.find_elements_by_xpath("//XCUIElementTypeCell/XCUIElementTypeStaticText")
            total_completed_workouts = len(completed_workouts[1:])
            print("Total completed workouts= " +str (total_completed_workouts))
            time.sleep(3)

            ## Check if all the workouts completed or not for that particular week ####
            total = 0
            for k in range(total_workouts):
                if k == 0:
                   k += 1
                workout_complete_checkmark = self.driver.find_elements_by_xpath("//XCUIElementTypeApplication[@name='Cheer District']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeButton")
                total_checkmark = len(workout_complete_checkmark)
                print ("Total completed workout in this week: " +str(total_checkmark))
                check_mark_value = workout_complete_checkmark[i].get_attribute('value')
                print(check_mark_value)
                total += int(check_mark_value)
                print("Total:" +str(total))
                if total == total_completed_workouts:
                    first_week.click()
                    number_weeks[i+1].click()

            ### Select the workout which is not completed #####
            for i in range(total_completed_workouts):
                if i == 0:
                    i += 1

                value = completed_workouts[i].get_attribute('value')
                print(value)

                #import pdb; pdb.set_trace()
                if value == '' or value is None:
                    time.sleep(3)
                    completed_workouts[i].click()
                    print("Let me see what is working")
                    ### If above condition works then exercises will be in the view #####
                    ### Counting total number of exercise and extracting the last digits ###
                    total_exercises = self.driver.find_element_by_id("ui_exercise_stats_text").get_attribute('value')
                    print(total_exercises)
                    print(total_exercises.split("/"))
                    #Total = int(total_exercises[3:-10])
                    Total = int(total_exercises[total_exercises.index('/') + 1:total_exercises.index(' ')])
                    print(Total)

                    continue_button = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='CONTINUE TRAINING']")
                    continue_button.click()
                    # self.elementClick(self._continue_training, locatorType='id')
                    start_button = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='START']")
                    # if start_button.is_displayed():
                    #     print("Start button is available")
                    for k in range(Total):
                        time.sleep(2)
                        duration = self.driver.find_element_by_id("ui_timer_label")
                        time_in_text = duration.get_attribute('value')
                        print(time_in_text)
                        x = time.strptime(time_in_text, '%M:%S')
                        print(x)
                        ##### convert time in text to seconds #############
                        time_in_seconds = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min, seconds=x.tm_sec).total_seconds()
                        print(time_in_seconds)
                        start_button.click()
                        time.sleep(2)
                        complete_button = self.driver.find_element_by_id("COMPLETE")
                        if complete_button.is_displayed():
                           complete_button.click()
                        else:
                            time.sleep(time_in_seconds)
                else:
                    print("Oops did not click next week tab")
                    #self.driver.find_element_by_xpath("//XCUIElementTypeStaticText[@name='Week #2']").click()

    @pytest.mark.run(order=1)
    def VerifyTrainingTabTest(self):
        self.clickTrainingTabTest()
        time.sleep(10)
        self.countworkoutsTest()
        time.sleep(10)







