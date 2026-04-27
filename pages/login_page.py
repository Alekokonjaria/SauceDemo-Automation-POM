from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login-button")

    def login(self, username, password):
        self.write(self.USERNAME, username)
        self.write(self.PASSWORD, password)
        self.click(self.LOGIN)