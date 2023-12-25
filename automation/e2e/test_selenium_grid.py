from selenium import webdriver
from automation.helpers.test_templates import TestCaseCC, check_value
from automation.pages.login import LogInPage
from selenium.webdriver.firefox.options import Options


class TestSeleniumGrid(TestCaseCC):

    def create_grid_driver(self, browser_name='firefox', grid_url='http://localhost:4444/wd/hub'):
        if browser_name.lower() == 'firefox':
            firefox_options = Options()
            # Add any Firefox-specific options here

            driver = webdriver.Remote(
                command_executor=grid_url,
                options=webdriver.FirefoxOptions()
            )
            return driver

    def test_grid(self, url, user, password):

        # region Prepare
        selenium_grid_url = "http://localhost:4444/wd/hub"
        # Instantiate an instance of Remote WebDriver with the desired capabilities.
        # t = check_value()
        driver = self.create_grid_driver()
        # driver = webdriver.Remote(command_executor=selenium_grid_url, options=webdriver.FirefoxOptions())
        login = LogInPage(driver)

        driver.get(url)
        # driver.find_element(By.ID, "login")

        login.login_musiconoff(user, password)
        print()
        print(driver.title, "was")
        driver.quit()
        # endregion Prepare
