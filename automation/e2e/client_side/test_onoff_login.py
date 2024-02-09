from selenium.webdriver.common.by import By
from automation.helpers.test_templates import TestCaseSelenium
from automation.pages.login import LogInPage


class TestMusicOnOff(TestCaseSelenium):

    def test_login(self, url, user, password):

        # region Prepare
        login = LogInPage(self.driver)
        self.driver.get(url)
        # endregion Prepare

        # region Action
        login.login_musiconoff(user, password)
        # endregion Action

        # region Validation
        assert login.wait.wait_until_present(By.ID, "search-albums")
        # endregion Validation
