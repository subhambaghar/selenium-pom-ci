from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.login(
        username="standard_user",
        password="secret_sauce"
    )
    inventory = InventoryPage(driver)
    inventory.add_backpack()

    assert inventory.get_cart_count() == '1'
    assert inventory.is_remove_button_visible()