
from pages.home.login_page import LoginPage
import pytest
from tests.configfile import EnvironmentSetup
from pages.Tabs.menu_page import MenuPage

class LoginTests(EnvironmentSetup):

    #@pytest.mark.run(order=1)
    @pytest.mark.first
    def test_validlogin(self):
        self.lp = LoginPage(self.driver)
        self.lp.validlogin("6471231231", "022455")
        self.lp.VerifyLoginSuccess()

    # #@pytest.mark.run(order=2)
    # @pytest.mark.second
    # def test_menutab(self):
    #     self.mn = MenuPage(self.driver)
    #     self.mn.VerifyMenutab()



    # @pytest.mark.run(order=1)
    # def test_Invalidlogin(self):
    #     self.lp = LoginPage(self.driver)
    #     self.lp.invalidlogin("")
    #     self.lp.VerifyLoginSuccess()
    #     self.driver.quit()

# if __name__ == "__main__":
#     LoginTests().test_validlogin()

    #ff = LoginTests()
    #ff.test_validlogin()
    #ff.tearDown()