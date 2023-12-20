from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from automation.helpers.test_templates import TestCaseCC
from automation.pages.login import LogInPage


chrome_driver_path = "/usr/local/bin/chromedriver"


class TestMusicOnOff(TestCaseCC):

    def test_login(self, browser, url, user, password):
        login = LogInPage(browser)
        print("Hello again! :)")
        browser.get(url)
        login.login_musiconoff(user, password)
        # driver.quit()

    def test_select_album(self, browser, url):
        pass

