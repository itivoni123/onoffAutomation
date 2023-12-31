import pytest
from automation.helpers.test_templates import TestCaseCC
from automation.pages.login import LogInPage


class TestSeleniumGrid(TestCaseCC):

    # @pytest.mark.parametrize()
    def test_grid(self, grid_driver, url, user, password):

        # region Prepare
        login = LogInPage(grid_driver)
        grid_driver.get(url)

        login.login_musiconoff(user, password)
        print()
        print(grid_driver.title, "was")
        grid_driver.save_screenshot("screenshot.png")
        grid_driver.quit()
        # endregion Prepare
