import pytest
from selenium.webdriver.common.by import By
import allure

from pages.shopping_page import ShoppingPage
from pages.login_page import LoginPage

@allure.feature("Shopping page")
@allure.story("Filter Functionality")
@pytest.mark.parametrize("sort_value, sort_type", [
    ("az","name"),
    ("za","name"),
    ("lohi", "price"),
    ("hilo", "price")
])

def test_all_filter(driver, sort_value, sort_type):
    login_page = LoginPage(driver)
    shopping_page = ShoppingPage(driver)

    with allure.step("Open Web Page, Insert user & password"):
        driver.get("https://www.saucedemo.com/")
        login_page.login("standard_user", "secret_sauce")

    shopping_page.select(sort_value)

    with allure.step(f"Checking {sort_type} sorting for filter: {sort_value}"):
        if sort_type == "price":
            price_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
            clear_price = [float(num.text.replace("$", "")) for num in price_elements]

            if sort_value == "lohi":
                assert clear_price == sorted(clear_price), f"Price is not Low to High: {clear_price}"
            else: # hilo
                assert clear_price == sorted(clear_price, reverse=True), f"Price is not High to Low: {clear_price}"

        elif sort_type == "name":
            name_elements = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
            name_text = [num.text for num in name_elements]

            if sort_value == "az":
                assert name_text == sorted(name_text), f"Names are not A-Z: {name_text}"
            else: # za
                assert name_text == sorted(name_text, reverse=True), f"Names are not Z-A: {name_text}"

