import time
import datetime
from base.selenium_driver import SeleniumDriver
from utilities.scroll_to_view_allworkouts import Scrolling
import utilities.custom_logger as cl
import logging
from pages.locators import Locator
import pytest
from appium.webdriver.common.touch_action import TouchAction



class TrainingProgress(Locator, SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        ### Getting Collapsed view week ####
        self.weekly_ui_element = lambda ele_num: self.driver.find_element_by_xpath(
            "(//XCUIElementTypeOther[@name='ui_section_week'])[{0}]".format(ele_num))

        ### Changing value of 1 to True and else to False for checked value ###
        self.change_to_boolean = lambda checked_value: True if checked_value == str(1) else False


    # Method to performance action on the elements
    def scrollUntilFindEle(self, ele):
        while True:
            try:
                ele_displayed = ele.is_displayed()
                if ele_displayed:
                    break
                else:
                    touch = TouchAction(self.driver)
                    touch.press(x=210, y=571).wait(500).move_to(x=210, y=400).release().perform()
                    time.sleep(2)
                    continue
            except:
                print('There is an error')
                break

    def clickTrainingTabTest(self):
        self.elementClick(self._switch_training_tab, locatorType="id")
        time.sleep(5)

    #count number of workouts available

    def countworkoutsTest(self):

        # self.scroll_until_find_ele()
        global exercise_num
        self.weekly_ui_element(1).click()
        print("Collapsed First Week !")

        ### Counting Total number of weeks ####
        weeks_ele = self.driver.find_elements_by_id("ui_section_week")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Total weeks: {0}".format(len(weeks_ele)))
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        ### Checking each week workout ####
        for num_week, week_ele in enumerate(weeks_ele):
            if num_week < 0:
                continue
            else:
                print("---------------------------------------------------")
                print("Week Number {0}".format(num_week+1))
                #### Scrolling up to see all the workouts in this week #####
                self.scrollUntilFindEle(self.weekly_ui_element(num_week+1))

                ### Opening up the acordion ###
                self.weekly_ui_element(num_week+1).click()

                ### Getting total number of workouts on particular week ###
                # workoutsList = self.driver.find_elements_by_xpath("//XCUIElementTypeCell/XCUIElementTypeButton")
                # print("Total workouts in this week: {0}".format(len(workoutsList)))

                time.sleep(2)

                weekly_workouts = self.driver.find_elements_by_xpath("//XCUIElementTypeCell/XCUIElementTypeButton")
                print("Total workouts in this week: {0}".format(len(weekly_workouts)))


                ### Getting completed workouts on that particular week ###
                workout_names = self.driver.find_elements_by_xpath("//XCUIElementTypeCell/XCUIElementTypeStaticText")
                print("Workout completion indicator and text present in this week (no need of print): {0}".format(
                    len(workout_names) - 1))  # First element doesn't need to be included
                time.sleep(3)
                print("---------------------------------------------------")

                ### Check mark counter ###
                total_check_marks = 0
                # weekly_workouts = self.driver.find_elements_by_xpath(
                #     "//XCUIElementTypeApplication[@name='Cheer District']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeButton")

                for num_workout, weekly_workout in enumerate(weekly_workouts):
                    print('Before Scroll')
                    self.scrollUntilFindEle(workout_names[2 * total_check_marks + 1])
                    print('After Scroll')
                    print("_____________")
                    weekly_workouts = self.driver.find_elements_by_xpath("//XCUIElementTypeApplication[@name='Cheer District']/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeButton")
                    checked = self.change_to_boolean(weekly_workouts[num_workout].get_attribute('value'))
                    print("Checked: {0}".format(checked))
                    print(total_check_marks, len(weekly_workouts))
                    print("_____________")
                    if checked:
                        total_check_marks += 1
                        print("Total checkmark in this week: {0}".format(total_check_marks))
                        ### All workouts are checked ###
                        if total_check_marks == len(weekly_workouts):
                            # click_weekly_ui_element(num_week+1)
                            self.weekly_ui_element(num_week+1).click()
                            # week_ele.click()
                            time.sleep(3)
                            break
                    else:
                        print("It is coming to else statement")
                        workout_names = self.driver.find_elements_by_xpath(
                            "//XCUIElementTypeCell/XCUIElementTypeStaticText")
                        # import pdb; pdb.set_trace()
                        #weekly_workouts[num_workout].click()
                        #workout_names[num_workout].click()
                        workout_names[2 * total_check_marks + 1].click()
                        time.sleep(3)

                        ### Separating exercises numbers from value ###
                        completed_exercises, total_exercises = \
                        self.driver.find_element_by_id("ui_exercise_stats_text").get_attribute('value').split(' ')[0].split(
                            '/')
                        remaining_exercises = int(total_exercises) - int(completed_exercises)
                        print("Completed Exercises: {0}, Total Exercises: {1}".format(completed_exercises, total_exercises))

                        ### Click on the continue button to go to exercise screen ###
                        continue_button = self.driver.find_element_by_xpath(
                            "//XCUIElementTypeButton[@name='CONTINUE TRAINING']")
                        continue_button.click()

                        for exercise_num in range(remaining_exercises+1):
                            print("start of the for-loop")
                            time.sleep(2)
                            duration = self.driver.find_element_by_id("ui_timer_label")
                            time.sleep(3)
                            exercise_time = time.strptime(duration.get_attribute('value'), '%M:%S')

                            print(exercise_time)
                            print("_____________")
                            print("Timer [m:ss]: {0}".format(exercise_time))

                            ##### convert time in text to seconds #############
                            time_in_seconds = datetime.timedelta(hours=exercise_time.tm_hour, minutes=exercise_time.tm_min,
                                                                 seconds=exercise_time.tm_sec).total_seconds()
                            print(time_in_seconds)
                            time.sleep(2)
                            start_button = self.driver.find_element_by_xpath("//XCUIElementTypeButton[@name='START']")
                            time.sleep(1)
                            start_button.click()

                            if time_in_seconds > 0:
                                print('NEED TO WAIT')
                                time.sleep(int(time_in_seconds)+2)
                                print('DONE WAITING')
                            else:
                                print('DONT NEED TO WAIT')
                                complete_button = self.driver.find_element_by_id("COMPLETE")
                                if complete_button.is_displayed():
                                    complete_button.click()
                                    time.sleep(2)
                                    print('CLICKED')
                                else:
                                    print("End of bljfslfjsdlfjsdl")

                        try:
                            if exercise_num == remaining_exercises:
                                print(exercise_num, remaining_exercises)
                                print("It is end of the workout")
                                # import pdb; pdb.set_trace()
                                time.sleep(3)
                                self.driver.find_element_by_id("DONE").click()
                                break
                        except Exception as unknown_error:
                            print('There was an error.\n {0}'.format(unknown_error))
                            continue



    @pytest.mark.run(order=1)
    def VerifyTrainingTabTest(self):
        self.clickTrainingTabTest()
        time.sleep(6)
        self.countworkoutsTest()
        time.sleep(10)