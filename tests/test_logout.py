from pages.login_page import LoginPage
from pages.menu_page import MenuPage

def test_logout(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    menu = MenuPage(driver)
    menu.logout()
    assert "saucedemo.com" in driver.current_url.lower()

