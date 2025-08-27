from pages.login_page import LoginPage

class TestLogin():
    def test_successfull(self):
        page = LoginPage()
        page.load()
        page.login("standard_user","secret_sauce")
        