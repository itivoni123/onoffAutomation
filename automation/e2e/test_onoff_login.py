from selenium.webdriver.common.by import By
from automation.helpers.test_templates import TestCaseCC
from automation.pages.login import LogInPage


class TestMusicOnOff(TestCaseCC):

    def test_login(self, browser, url, user, password):

        # region Prepare
        login = LogInPage(browser)
        print("Hello again! :)")
        browser.get(url)
        # endregion Prepare

        # region Action
        login.login_musiconoff(user, password)
        # endregion Action

        # region Validation
        assert login.wait.wait_until_present(By.ID, "search-albums")
        # endregion Validation

    def test_select_album(self, browser, url):
        pass
