import logging

import pytest

from automation.helpers.test_templates import TestCaseSeleniumGrid
from automation.pages.login import LogInPage


class TestSeleniumGrid(TestCaseSeleniumGrid):

    @pytest.fixture
    def login(self):
        return LogInPage(self.driver)

    def test_grid(self, url, user, password, login):
        # region prepare
        self.driver.get(url)
        # endregion Prepare

        # region Action
        is_user_logged_in = login.login_musiconoff(user, password)
        logging.info("all good :)")
        self.driver.save_screenshot("screenshot.png")
        # endregion Action

        # region ValidationLogInPage
        assert is_user_logged_in
        assert login.logout_musiconoff()
        # endregion Validation

    def test_logout_onoff(self, url, user, password, login):

        # region Prepare
        self.driver.get(url)

        login.login_musiconoff(user, password)
        self.driver.save_screenshot("screenshot.png")
        login.logout_musiconoff()
        # endregion Prepare
