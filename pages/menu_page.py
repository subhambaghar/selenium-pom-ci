from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MenuPage:
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    def logout(self):
        self.wait.until(EC.element_to_be_clickable(self.MENU_BUTTON)).click()
        self.wait.until(EC.visibility_of_element_located(self.LOGOUT_BUTTON)).click()