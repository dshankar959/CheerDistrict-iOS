from appium.webdriver.common.touch_action import TouchAction
from pages.locators import Locator
import time

class Scrolling(Locator):
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, destination_element, direction ="down", click = False):
        visibility = False
        # Scroll until element is visible
        while (visibility == False):
            try:
                # Trying to identify the element in first attempt
                #destination_element = self.driver.find_element_by_accessibility_id(self._ViewAll)
                destination_element = self.driver.find_element_by_accessibility_id(self._friends)
                time.sleep(2)

                visibility = destination_element.is_displayed()
                # Add this condition as some elements are able to be identified by the driver but still are not visible.
                if not visibility:
                    raise Exception
            except:
                # Use execute script instead of TouchAction because TouchAction needs the element to be visible.
                self.driver.execute_script("mobile: scroll", {"direction": direction})

                if(click):

                    destination_element.click()
                else:
                    return destination_element