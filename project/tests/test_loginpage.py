# Sayfa tanımlarını kullanarak aksiyonların ilgili case'e göre farklı farklı çalıştırılıp
# test edilmesi.
from pages.login_page import LoginPage
from utils.image_helper import save_screenshot

class TestLogin():
    def test_successfull(self, driver, waiter):
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

    def test_username_empty(self, driver, waiter):
        page = LoginPage(driver,waiter)
        page.load()
        page.login("","secret_sauce123")
        save_screenshot(driver, "test_username_empty")
        assert page.get_error_message() == "Epic sadface: Username is required" 
