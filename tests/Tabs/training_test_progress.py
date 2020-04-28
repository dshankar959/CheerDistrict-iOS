from tests.configfile import EnvironmentSetup
from pages.Tabs.Timeline_page import TimelinePage
from pages.Tabs.Create_post import CreatePost
from utilities.scroll_recent_post import Scrolling
from utilities.teststatus import TestStatus
from utilities.screenshot import Screenshottest
from pages.Tabs.Trainingprogress import TrainingProgress


class TrainingTabTest(EnvironmentSetup):
    def test_TrainingTab(self):
        self.ts = TestStatus(self.driver)
        self.tn = TrainingProgress(self.driver)
        result1 = self.tn.VerifyTrainingTabTest()
        self.ts.mark(result1, "Training Tab Verification")
