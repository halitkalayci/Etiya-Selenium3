from pages.login_page import LoginPage
from utils.image_helper import save_screenshot

class TestLogin():
    def test_successfull(self,driver,waiter):
        page = LoginPage(driver,waiter)
        page.load()
        page.login("standard_user","secret_sauce")
        save_screenshot(driver, "test_successfull")
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"
    
    def test_invalid_user(self, driver, waiter):
        page = LoginPage(driver,waiter)
        page.load()
        page.login("standard_user","secret_sauce123")
        save_screenshot(driver, "test_invalid_user")
        assert page.get_error_message() == "Epic sadface: Username and password do not match any user in this service" 