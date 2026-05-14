from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


#1 Find elements

class ShoppingPage(BasePage):

    
    SELECT_FILTER = (By.CLASS_NAME, 'product_sort_container')

    def select(self,value):
        dropdown_element = self.driver.find_element(*self.SELECT_FILTER)

        select = Select(dropdown_element)

        select.select_by_value(value)

