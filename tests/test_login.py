import pytest
pytest.skip("Deprecated: split into positive/negative tests", allow_module_level=True)
import time
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_login_for_standard_user(driver):
    login_page = LoginPage(driver)
    login_page.login(
        username="standard_user",
        password="secret_sauce"
    )
    logo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert logo.is_displayed()
    assert logo.text == 'Swag Labs'

def test_login_for_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.login(
        username="locked_out_user",
        password="secret_sauce"
    )
    error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert error.is_displayed()
    assert error.text == "Epic sadface: Sorry, this user has been locked out."
@pytest.mark.xfail(reason="Known issue: problem_user has broken product images (sl-404)")
def test_login_for_problem_user(driver):
    login_page = LoginPage(driver)
    login_page.login(
        username="problem_user",
        password="secret_sauce"
    )
    logo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert logo.is_displayed()

    images = driver.find_elements(By.CLASS_NAME, "inventory_item_img")
    for img in images:
        src = img.get_attribute("src") or ""
        assert 'sl-404' not in src.lower()
def test_login_for_performance_glitch_user(driver):
    login_page = LoginPage(driver)
    login_page.login(
        username="problem_user",
        password="secret_sauce"
    )
    start = time.time()
    driver.find_element(By.CLASS_NAME, "app_logo")
    duration = time.time() - start
    assert duration < 5, f"Login too slow: {duration} seconds"
def test_login_for_visual_user(driver):
    login_page = LoginPage(driver)
    login_page.login(
        username="visual_user",
        password="secret_sauce"
    )
    logo = driver.find_element(By.CLASS_NAME, "app_logo")
    assert logo.is_displayed()

    titles = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert len(titles) > 0
def test_login_with_no_credentials(driver):
    login_page = LoginPage(driver)
    login_page.login(username="", password="")
    error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert error.is_displayed()
    assert "username is required" in error.text.lower()
def test_login_with_username_only(driver):
    login_page = LoginPage(driver)
    login_page.login(username="standard_user", password="")
    error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert "password is required" in error.text.lower()
def test_login_with_password_only(driver):
    login_page = LoginPage(driver)
    login_page.login(username="", password="secret_sauce")
    error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert "username is required" in error.text.lower()
