from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_purchase_flow(driver):
    login_pg = LoginPage(driver)
    checkout_pg = CheckoutPage(driver)
    inventory_pg = InventoryPage(driver)

    driver.get("https://www.saucedemo.com/")
    login_pg.login("standard_user", "secret_sauce")

    inventory_pg.add_all_items()
    assert inventory_pg.get_cart_count() == "6"
    inventory_pg.go_to_cart()

    checkout_pg.checkout()
    checkout_pg.fill_fields("Henry", "Cavill", "012")
    checkout_pg.finish_checkout()

    assert checkout_pg.check_succses() == "Thank you for your order!"
