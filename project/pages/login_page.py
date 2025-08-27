from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
class LoginPage():
    def __init__(self, driver:Chrome, wait:WebDriverWait):
        self.driver = driver
        self.wait = wait
        # Sayfa özelliklerini tanımla.
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_container = (By.CSS_SELECTOR, "[data-test='error']")

    def load(self):
        self.driver.get("https://saucedemo.com")
        self.wait.until(expected_conditions.visibility_of_element_located(self.username_input))

    def login(self, username, password):
        self.wait.until(expected_conditions.visibility_of_element_located(self.username_input)).send_keys(username)
        self.wait.until(expected_conditions.visibility_of_element_located(self.password_input)).send_keys(password)
        self.wait.until(expected_conditions.visibility_of_element_located(self.login_button)).click()

    def get_error_message(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.error_container)).text