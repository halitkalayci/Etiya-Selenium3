from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time 
driver = Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")

h3 = driver.find_element(By.XPATH, "//*[@id='content']/div/h3")
print(h3.text)
time.sleep(3)

iframe = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(iframe)

time.sleep(3)
p = driver.find_element(By.XPATH, "//*[@id='tinymce']/p")
print(p.text)

