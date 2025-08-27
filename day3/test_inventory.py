from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest

class TestInventory():
    def test_add_item_to_cart(self,driver):
        waiter = WebDriverWait(driver, 10)
        driver.get("https://www.saucedemo.com/")
        username_input = waiter.until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))   
        username_input.send_keys("standard_user")
        waiter.until(expected_conditions.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
        waiter.until(expected_conditions.element_to_be_clickable((By.ID, "login-button"))).click()
        waiter.until(expected_conditions.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        cart_badge = waiter.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")))
        assert cart_badge.text == "1"