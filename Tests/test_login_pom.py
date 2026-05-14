import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@allure.feature("Login")
@allure.story("Valid Login")
def test_login(driver):
#1: Page Object Creation
    login_pg = LoginPage(driver)

#2: Getting Web Page
    with allure.step("Open Web Page"):
        driver.get("https://www.saucedemo.com/")

#3: Input information
    with allure.step("Insert user & password"):
        login_pg.login("standard_user", "secret_sauce")

#4: Assertation
    with allure.step("Check authorization"):
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

    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "6")
    )
    assert inventory_pg.get_cart_count() == "6"