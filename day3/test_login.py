from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest

class TestLogin():
    @pytest.mark.skip
    def test_success(self):
        #Arrrange
        driver = Chrome()
        driver.maximize_window()
        waiter = WebDriverWait(driver, 10)
        #
        #Act
        driver.get("https://www.saucedemo.com/")
        username_input = waiter.until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))   
        username_input.send_keys("standard_user")
        waiter.until(expected_conditions.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
        waiter.until(expected_conditions.element_to_be_clickable((By.ID, "login-button"))).click()
        #Assert
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    
    # Decorator -> Fonksiyonun içeriğini düzenlemeden çalışma mantığını genişletmek/düzenlemek.
    @pytest.mark.parametrize("username,password", [ ("abc123","abc123"), ("myuser","mypassword"), ("123","123") ])
    def test_invalid_user(self, username, password):
        driver = Chrome()
        driver.maximize_window()
        waiter = WebDriverWait(driver, 10) 
        driver.get("https://www.saucedemo.com/")
        username_input = waiter.until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))  
        username_input.send_keys(username)
        waiter.until(expected_conditions.visibility_of_element_located((By.ID,"password"))).send_keys(password)
        waiter.until(expected_conditions.element_to_be_clickable((By.ID, "login-button"))).click()
        error_h3 = waiter.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")))
        assert error_h3.text == "Epic sadface: Username and password do not match any user in this service"
        