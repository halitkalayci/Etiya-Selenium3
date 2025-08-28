from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class InventoryPage():
    def __init__(self, driver:Chrome, wait:WebDriverWait):
        self.driver=driver
        self.wait=wait
        self.cart_icon = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
        self.cart_badge = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")

        self.main_container = (By.CSS_SELECTOR, "[data-test='inventory-list']")
        self.products = (By.CLASS_NAME, "inventory_item") 
    
    def get_products(self):
        container = self.wait.until(expected_conditions.visibility_of_element_located(self.main_container))
        return container.find_elements(*self.products)
    