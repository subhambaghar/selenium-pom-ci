from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    ADD_BACKPACK = (By.ID, 'add-to-cart-sauce-labs-backpack')
    CART_BADGE = (By.CLASS_NAME, 'shopping_cart_badge')
    REMOVE_BTN = (By.ID, 'remove-sauce-labs-backpack')
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    def add_backpack(self):
        self.wait.until(EC.visibility_of_element_located(self.ADD_BACKPACK)).click()
    def get_cart_count(self):
        badge = self.wait.until(EC.visibility_of_element_located(self.CART_BADGE))
        return badge.text
    def is_remove_button_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.REMOVE_BTN)).is_displayed()