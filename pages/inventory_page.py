import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class InventoryPage(BasePage):

#1: Finding and Testing Buttons
    ADD_TO_CARTS_BTNS = (By.CLASS_NAME, "btn_inventory")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def add_all_items(self):
        button = self.driver.find_elements(*self.ADD_TO_CARTS_BTNS)

        for btn in button:
            button = self.driver.find_element(By.XPATH, "//button[text()='Add to cart']")
            self.driver.execute_script("arguments[0].scrollIntoView();", btn)
            button.click()
            time.sleep(0.3)

    def get_cart_count(self):

        return self.get_text(self.CART_BADGE)

    def go_to_cart(self):
        self.click(self.CART_LINK)