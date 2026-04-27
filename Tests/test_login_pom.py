import pytest
from selenium import webdriver
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_login(driver):
#1: Page Object Creation
    login_pg = LoginPage(driver)
#2: Getting Web Page
    driver.get("https://www.saucedemo.com/")
#3: Input information
    login_pg.login("standard_user", "secret_sauce")
#4: Assertation
    assert "inventory" in driver.current_url

def test_full_purchase_flow(driver):
    login_pg = LoginPage(driver)
    inventory_pg = InventoryPage(driver)

#1: Login In
    driver.get("https://www.saucedemo.com/")
    login_pg.login("standard_user", "secret_sauce")

#2: Add product
    inventory_pg.add_all_items()

#3: Assertation - Check if 6 product
    assert inventory_pg.get_cart_count() == "6"