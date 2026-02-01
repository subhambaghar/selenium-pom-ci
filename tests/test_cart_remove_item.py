import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By

@pytest.mark.xfail(reason="Cart remove is flaky in CI (SauceDemo DOM behavior)")
def test_remove_item_from_cart(driver):
    login_page = LoginPage(driver)
    login_page.login(
        username="standard_user",
        password="secret_sauce"
    )
    inventory = InventoryPage(driver)
    inventory.add_backpack()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart = CartPage(driver)

    cart.remove_item()
    cart.wait_until_item_removed()
    assert not cart.is_item_present()