from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from project.pages.login_page import LoginPage


class InventoryPage():
    def __init__(self, driver:Chrome, wait:WebDriverWait):
        self.driver=driver
        self.wait=wait
        self.cart_icon = (By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
        self.cart_badge = (By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")

        self.main_container = (By.CSS_SELECTOR, "[data-test='inventory-list']")
        self.products = (By.CLASS_NAME, "inventory_item") 

    def load(self, username="standard_user", password="secret_sauce"):
        login_page = LoginPage(self.driver, self.wait)   
        login_page.load()
        login_page.login(username,password)
        self.driver.get("https://saucedemo.com/inventory.html")
        self.wait.until(expected_conditions.visibility_of_element_located(self.cart_icon))
    
    def get_products(self):
        container = self.wait.until(expected_conditions.visibility_of_element_located(self.main_container))
        return container.find_elements(*self.products)

    def add_to_cart(self, product_test_id):
        selector = (By.CSS_SELECTOR, f"[data-test='add-to-cart-{product_test_id}']")
        self.wait.until(expected_conditions.element_to_be_clickable(selector)).click()
    
    def get_cart_badge_text(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.cart_badge)).text