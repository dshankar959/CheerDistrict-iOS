from tests.configfile import EnvironmentSetup
from pages.Tabs.Timeline_page import TimelinePage
from pages.Tabs.Create_post import CreatePost
from utilities.scroll_recent_post import Scrolling
from utilities.teststatus import TestStatus
from utilities.screenshot import Screenshottest

class CreatePostTest(EnvironmentSetup):

    def test_Createpost(self):
        self.cp = CreatePost(self.driver)
        self.ts = TestStatus(self.driver)
        result1 = self.cp.VerifyCreatePost()
        tc = Scrolling(self.driver)
        tc.scroll_to_element(self)
        self.ts.mark(result1, "Create Post Verification")
