import pytest
from selenium import webdriver


class Browser(object):
    grid_url = 'http://localhost:4444/wd/hub'

    def grid_browser(self, browser_type):
        driver_class = {

                "chrome": webdriver.Remote(
                    command_executor=self.grid_url,
                    options=webdriver.ChromeOptions()

                ),
                "firefox": webdriver.Remote(
                    command_executor=self.grid_url,
                    options=webdriver.FirefoxOptions()

                ),
                "edge": webdriver.Remote(
                    command_executor=self.grid_url,
                    options=webdriver.EdgeOptions()

                ),
            }
        return driver_class[browser_type]
