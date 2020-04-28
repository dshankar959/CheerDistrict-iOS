from tests.configfile import EnvironmentSetup
from pages.Tabs.Timeline_page import TimelinePage
from pages.Tabs.Create_post import CreatePost
from utilities.scroll_recent_post import Scrolling
from utilities.teststatus import TestStatus
from pages.Tabs.test_swipe import Swipe


class SwipeTest(EnvironmentSetup):

    def test_Swipeup(self):
        self.sp = Swipe(self.driver)
        self.ts = TestStatus(self.driver)
        result1 = self.sp.VerifySwipe()
        self.ts.mark(result1, "Training Tab Verification")