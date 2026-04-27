from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class CheckoutPage(BasePage):

    CHECKOUT = (By.ID, 'checkout')
    GET_FIRST_NAME = (By.ID, "first-name")
    GET_LAST_NAME = (By.ID, "last-name")
    GET_ZIP_POSTAL_CODE = (By.ID, "postal-code")
    FINISH = (By.ID, "finish")
    CONTINUE = (By.ID, "continue")
    COMPLETE = (By.CLASS_NAME, "complete-header")

    def checkout(self):
        self.click(self.CHECKOUT)

    def fill_fields(self, first_name, last_name, zip_postal_code):
        self.write(self.GET_FIRST_NAME, first_name)
        self.write(self.GET_LAST_NAME, last_name)
        self.write(self.GET_ZIP_POSTAL_CODE, zip_postal_code)
        self.click(self.CONTINUE)

    def finish_checkout(self):
        self.click(self.FINISH)

    def check_succses(self):
        return self.get_text(self.COMPLETE)
