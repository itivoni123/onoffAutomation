from selenium.webdriver.firefox.options import Options
from selenium import webdriver


class TestCaseCC(object):

    def create_grid_driver(self, browser_name='firefox', grid_url='http://localhost:4444/wd/hub'):
        if browser_name.lower() == 'firefox':
            firefox_options = Options()
            # Add any Firefox-specific options here

            driver = webdriver.Remote(
                command_executor=grid_url,
                options=webdriver.ChromeOptions()
            )
            return driver

    def teardown_method(self):
        pass
