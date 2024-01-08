from selenium.webdriver.common.by import By
from automation.pages.files_elements import LoginElements, AlbumsElements
from automation.pages.waiting_to import WaitToElement


class LogInPage(LoginElements, AlbumsElements):
    def __init__(self, browser):
        self.wait = WaitToElement(browser)
        self.browser = browser

    def login_musiconoff(self, username, password):
        self.wait.wait_until_present(By.ID, self.ID_LOGIN)
        self.browser.find_element(By.ID, self.ID_LOGIN).click()
        self.wait.wait_until_present(By.ID, self.ID_LOGIN_BTN)
        cred_user = self.browser.find_element(By.NAME, "username")
        cred_pass = self.browser.find_element(By.NAME, "password")
        cred_user.send_keys(username)
        cred_pass.send_keys(password)
        self.browser.find_element(By.ID, self.ID_LOGIN_BTN).click()
        self.wait.wait_until_present(By.ID, self.ID_ALBUMS_RELEASED_TITLE)

    def logout_musiconoff(self):
        self.wait.wait_until_present(By.ID, self.ID_LOGOUT_BTN)
        self.browser.find_element(By.ID, self.ID_LOGOUT_BTN).click()
        self.wait.wait_until_present(By.ID, self.ID_LOGIN_AGAIN_LINK)
