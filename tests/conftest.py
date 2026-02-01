import pytest
import time
import os
from utils.driver_factory import get_driver

@pytest.fixture
def driver():
    driver = get_driver()
    driver.get("https://www.saucedemo.com")
    yield driver
    # time.sleep(5)
    driver.quit()
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' or report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"{item.name}_{timestamp}.png"
            driver.save_screenshot(os.path.join(screenshots_dir, filename))