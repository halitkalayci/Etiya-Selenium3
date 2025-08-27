import pytest
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# PyTest tarafından tüm test caseler öncesi kontrol edilen global dosya.

@pytest.fixture 
def driver():
    driver = Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def waiter(driver):
    waiter = WebDriverWait(driver, 10)
    yield waiter