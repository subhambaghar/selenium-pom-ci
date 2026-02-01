from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    CART_ITEM = (By.CLASS_NAME, 'cart_item')
    ITEM_NAME = (By.CLASS_NAME, 'inventory_item_name')
    CART_QTY = (By.CLASS_NAME, 'cart_quantity')
    ITEM_PRICE = (By.CLASS_NAME, 'inventory_item_price')
    REMOVE_BTN = (By.ID, 'remove-sauce-labs-backpack')
    CHECKOUT_BTN = (By.ID, 'checkout')

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    # 1️⃣ Item added appears in cart
    # 2️⃣ Correct item name
    # 3️⃣ Correct quantity (QTY = 1)
    # 4️⃣ Correct price
    # 5️⃣ Remove button works
    # 6️⃣ Checkout button is visible

    def is_item_present(self):
        return len(self.driver.find_elements(*self.ITEM_NAME)) > 0
    def get_item_name(self):
        return self.wait.until(EC.visibility_of_element_located(self.ITEM_NAME)).text
    def get_item_quantity(self):
        return self.wait.until(EC.visibility_of_element_located(self.CART_QTY)).text
    def get_item_price(self):
        return self.wait.until(EC.visibility_of_element_located(self.ITEM_PRICE)).text
    def remove_item(self):
        self.wait.until(EC.element_to_be_clickable(self.REMOVE_BTN)).click()
    def wait_until_item_removed(self):
        self.wait.until(EC.invisibility_of_element_located(self.REMOVE_BTN))
    def is_checkout_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.CHECKOUT_BTN)).is_displayed()