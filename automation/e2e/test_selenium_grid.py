import logging
import pytest
from selenium import webdriver

from automation.helpers.test_templates import TestCaseCC
from automation.pages.login import LogInPage


class TestSeleniumGrid(TestCaseCC):

    # @pytest.mark.parametrize("browsers_type", ["chrome", "firefox", "edge"],)
    # @pytest.mark.usefixtures("chrome_browser")
    def test_grid(self, url, user, password, chrome_browser):

        # region Prepare
        # driver_browsers = self.grid_browser()
        print(chrome_browser["browser_name"], "keys")
        driver = chrome_browser["driver"]
        login = LogInPage(driver)
        driver.get(url)

        login.login_musiconoff(user, password)
        logging.info("all good :)")
        driver.save_screenshot("screenshot.png")
        # print(my_fixture['key'], "kiki")
        # assert 'key' in my_fixture
        # assert my_fixture['key'] == 'value'
        # driver.quit()
        # endregion Prepare

    def test_logout_onoff(self, grid_driver, url, user, password):

        # region Prepare
        login = LogInPage(grid_driver)
        grid_driver.get(url)

        login.login_musiconoff(user, password)

        print(grid_driver.title, "was")
        grid_driver.save_screenshot("screenshot.png")
        login.logout_musiconoff()
        grid_driver.quit()
        # endregion Prepare
