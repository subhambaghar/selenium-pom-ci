import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

@pytest.mark.regression
@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        ("", "", "username is required"),
        ("standard_user", "", "password is required"),
        ("", "secret_sauce", "username is required"),
        ("locked_out_user", "secret_sauce", "locked out"),
    ]
)
def test_login_negative_users(driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.login(username, password)

    error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert error.is_displayed()
    assert expected_error in error.text.lower()