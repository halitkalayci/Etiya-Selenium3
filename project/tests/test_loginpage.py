from pages.login_page import LoginPage

class TestLogin():
    def test_successfull(self,driver,wait):
        page = LoginPage(driver,wait)
        page.load()
        page.login("standard_user","secret_sauce")
        assert driver.current_url == "https://www.saucedemo.com/inventory.html"