from seleniumwire import webdriver
from selenium.webdriver.firefox.options import Options


def check_value(grid_url='http://localhost:4444/wd/hub'):
    print("walla walla walla")
    driver = webdriver.Remote(
        command_executor=grid_url,
        options=webdriver.FirefoxOptions()
    )
    return driver

class TestCaseCC(object):


    def teardown_method(self):
        pass
