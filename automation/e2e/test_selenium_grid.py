import logging
from automation.helpers.test_templates import TestCaseCC
from automation.pages.login import LogInPage


class TestSeleniumGrid(TestCaseCC):

    def test_grid(self, url, user, password):
        # region prepare
        login = LogInPage(self.driver)
        self.driver.get(url)
        # endregion Prepare

        # region Action
        login.login_musiconoff(user, password)
        logging.info("all good :)")
        self.driver.save_screenshot("screenshot.png")
        # endregion Action

    def test_logout_onoff(self, url, user, password):

        # region Prepare
        login = LogInPage(self.driver)
        self.driver.get(url)

        login.login_musiconoff(user, password)
        self.driver.save_screenshot("screenshot.png")
        login.logout_musiconoff()
        self.driver.quit()
        # endregion Prepare
