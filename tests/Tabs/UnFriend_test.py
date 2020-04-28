from tests.configfile import EnvironmentSetup
from pages.Tabs.UnFriend import DeleteFriend
from utilities.scroll_to_Friends import Scrolling
from utilities.teststatus import TestStatus
from utilities.screenshot import Screenshottest


class DeleteFriendTest(EnvironmentSetup):

    def test_DeleteFriend(self):
        self.df = DeleteFriend(self.driver)
        self.ts = TestStatus(self.driver)
        result1 = self.df.VerifySelectProfile()
        tc = Scrolling(self.driver)
        tc.scroll_to_element(self)
        result2 = self.df.VerifySeeAllFriends()
        self.ts.mark(result1, "Delete friend Verification")
        self.ts.mark(result2, "Friend list has been selected")
