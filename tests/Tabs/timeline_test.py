from tests.configfile import EnvironmentSetup
from pages.Tabs.Timeline_page import TimelinePage
from utilities.scroll_recent_post import Scrolling
from utilities.teststatus import TestStatus
from utilities.screenshot import Screenshottest

class TimelineTest(EnvironmentSetup):

    def test_viewall(self):
        tc = Scrolling(self.driver)
        tc.scroll_to_element(self)
        self.tl = TimelinePage(self.driver)
        self.tl.VerifyViewAll()
        for i in range(5):
            tc.scroll_to_element(self)
            self.tl = TimelinePage(self.driver)
            self.tl.VerifyViewAll()

