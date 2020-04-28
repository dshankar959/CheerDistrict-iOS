
from selenium.webdriver.common.by import By
from appium import webdriver
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os

class Screenshottest():
        log = cl.customLogger(logging.DEBUG)

        def __init__(self, driver):
            self.driver = driver

        def screenShot(self, resultMessage):
            """
            Takes screenshot of the current open web page
            """
            fileName = str(resultMessage) + "." + str(round(time.time() * 1000)) + ".png"
            screenshotDirectory = "../screenshots/"
            relativeFileName = screenshotDirectory + fileName
            currentDirectory = os.path.dirname(__file__)
            destinationFile = os.path.join(currentDirectory, relativeFileName)
            destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

            try:
                if not os.path.exists(destinationDirectory):
                    os.makedirs(destinationDirectory)
                self.driver.save_screenshot(destinationFile)
                self.log.info("Screenshot save to directory: " + destinationFile)
            except:
                self.log.error("### Exception Occurred when taking screenshot")
                print_stack()