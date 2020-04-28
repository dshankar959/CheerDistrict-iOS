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
        ### Getting Collapsed view week ####
        #self.elementClick(self._first_week, locatorType="xpath")
        first_week = self.driver.find_element_by_xpath("(//XCUIElementTypeOther[@name='ui_section_week'])[1]")
        first_week.click()

        ### Counting Total number of weeks ####
        number_weeks= self.driver.find_elements_by_id("ui_section_week")
        #number_weeks = self.driver.find_elements(self._number_weeks, locatorType="id")
        total_weeks = len(number_weeks)
        print("Total weeks= "+str(total_weeks))

        ### Checking each week workout ####

        for i in range(total_weeks):
            print("i=" +str(i))
            #number_weeks = self.driver.find_elements(self._number_weeks, locatorType="id")
            number_weeks = self.driver.find_elements_by_id("ui_section_week")
            number_weeks[i].click()

            ### Getting total number of workouts on particular week ##
            workoutsList = self.driver.find_elements_by_xpath("//XCUIElementTypeCell/XCUIElementTypeButton")
            total_workouts = len(workoutsList)
            print("Total workouts in this week: " + str(total_workouts))

            # ## Getting completed workouts on that particular week ##
            workout_names = self.driver.find_elements_by_xpath("//XCUIElementTypeCell/XCUIElementTypeStaticText")
            total_text = len(workout_names[1:])
            print("Workout completion indicator and text present in this week (no need of print)= " +str (total_text))
            time.sleep(3)

            total = 0
            for k in range(total_workouts):
                if k == 0:
                    k += 1
                workout_complete_checkmark = self.driver.find_elements_by_xpath(
                    "//XCUIElementTypeApplication[@name='Cheer District']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeButton")
                total_checkmark = len(workout_complete_checkmark)
                print("Checkmark and workout name counts: " + str(total_checkmark))
                check_mark_value = workout_complete_checkmark[i].get_attribute('value')
                print("value = " + check_mark_value)
                print("_____________")
                if int(check_mark_value) == 1:
                    total += int(check_mark_value)
                    print("Total checkmark in this week:" + str(total))
                    if total == total_workouts:
                        first_week = self.driver.find_element_by_xpath(
                            "(//XCUIElementTypeOther[@name='ui_section_week'])[1]")
                        first_week.click()
                        time.sleep(3)
                        break

                else:
                    for k in range(total_workouts):
                        if k > 0:
                            check_mark_value2 = workout_complete_checkmark[k].get_attribute('value')
                            print(check_mark_value2)
                            if check_mark_value2 == '' or check_mark_value is None:
                                time.sleep(3)
                                workout_names[i].click()
                                time.sleep(2)
                                print("Until this point it is working")

                                ### If above condition works then exercises will be in the view #####

                                ### Counting total number of exercise and extracting the last digits ###
                                total_exercises = self.driver.find_element_by_id("ui_exercise_stats_text").get_attribute('value')
                                print(total_exercises)
                                print(total_exercises.split("/"))
                                # Total = int(total_exercises[3:-10])
                                Total1 = int(total_exercises[total_exercises.index('/') + 1:total_exercises.index(' ')])
                                print(Total1)

                                continue_button = self.driver.find_element_by_xpath(
                                    "//XCUIElementTypeButton[@name='CONTINUE TRAINING']")
                                continue_button.click()
                                # self.elementClick(self._continue_training, locatorType='id')

                                start_button = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='START']")
                                # if start_button.is_displayed():
                                #     print("Start button is available")

                                for k in range(Total1):
                                    time.sleep(3)
                                    duration = self.driver.find_element_by_id("ui_timer_label")
                                    time.sleep(3)
                                    time_in_text = duration.get_attribute('value')
                                    print(time_in_text)
                                    x = time.strptime(time_in_text, '%M:%S')
                                    print(x)
                                    ##### convert time in text to seconds #############
                                    time_in_seconds = datetime.timedelta(hours=x.tm_hour, minutes=x.tm_min,
                                                                         seconds=x.tm_sec).total_seconds()
                                    print(time_in_seconds)
                                    start_button.click()
                                    time.sleep(2)
                                    complete_button = self.driver.find_element_by_id("COMPLETE")
                                    if complete_button.is_displayed():
                                        complete_button.click()
                                    else:
                                        time.sleep(time_in_seconds)

    @pytest.mark.run(order=1)
    def VerifyTrainingTabTest(self):
        self.clickTrainingTabTest()
        time.sleep(10)
        self.countworkoutsTest()
        time.sleep(10)







