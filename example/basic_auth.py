from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time 

driver = Chrome()
# Basic Auth. varsa, url ile çözülebilir.
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
p = driver.find_element(By.XPATH, "//*[@id='content']/div/p")

print(p.text)