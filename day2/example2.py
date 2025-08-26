from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time 


driver = Chrome()
driver.maximize_window()
driver.get("https://books-pwakit.appspot.com/")

# driveri tanımladık -> MAIN DOM
book_app = driver.find_element(By.TAG_NAME, "book-app")

shadow_root = book_app.shadow_root

search_input = shadow_root.find_element(By.ID, "input")
search_input.send_keys("Orhan Pamuk")
time.sleep(30)