import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

@pytest.mark.smoke
@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("visual_user", "secret_sauce"),
    ]
)
def test_login_positive_users(driver, username, password):
    login_page = LoginPage(driver)
    login_page.login(username, password)

    logo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert logo.is_displayed()
    assert logo.text == 'Swag Labs'