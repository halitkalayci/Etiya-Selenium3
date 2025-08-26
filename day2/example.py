from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By

driver = Chrome() #manual kurulum?
driver.get("https://www.saucedemo.com/")

# tüm htmlde id="user-name" olan elementi bul.
username_input = driver.find_element(By.ID, "user-name") #locate
# elementi buldu.
username_input.send_keys("standard_user")

driver.find_element(By.ID, "password").send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").click()
# FluentWait -> Selenium alt modülü.
time.sleep(30) 