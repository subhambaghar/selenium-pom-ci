import pytest
import time
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

@pytest.mark.xfail(reason="Known SauceDemo defects for specific users")
@pytest.mark.parametrize(
    "username",
    [
        "problem_user"
    ]
)
def test_login_known_defect_users(driver, username):
    login_page = LoginPage(driver)
    login_page.login(username, "secret_sauce")

    logo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert logo.is_displayed()

@pytest.mark.xfail(reason="Known performance issue: slow login")
def test_login_performance_glitch_user(driver):
    start_time = time.time()
    login_page = LoginPage(driver)
    login_page.login("performance_glitch_user", "secret_sauce")

    driver.find_element(By.CLASS_NAME, "app_logo")
    duration = time.time() - start_time

    assert duration < 5, f"Login too slow: {duration} seconds"