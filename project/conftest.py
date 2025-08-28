# conftest.py -> PyTest'in tüm testler için çalıştırma öncesi-sonrası kontrol ettiği global dosya.

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

# PyTest tarafından tüm test caseler öncesi kontrol edilen global dosya.

@pytest.fixture 
def driver():
    options = Options()
    #options.add_argument("--headless")
    driver = Chrome(options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture # dependency injection
def waiter(driver):
    waiter = WebDriverWait(driver, 10)
    yield waiter