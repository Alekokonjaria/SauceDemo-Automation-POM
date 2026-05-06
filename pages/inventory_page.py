from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

class InventoryPage(BasePage):

#1: Finding and Testing Buttons
    ADD_TO_CARTS_BTNS = (By.CLASS_NAME, "btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_all_items(self):
        button = self.driver.find_elements(*self.ADD_TO_CARTS_BTNS)

        for btn in button:
            btn.click()
    def get_cart_count(self):

        return self.get_text(self.CART_BADGE)

    def go_to_cart(self):
        self.click(self.CART_LINK)