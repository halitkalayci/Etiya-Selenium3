from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time 
from requests import get

driver = Chrome()
driver.get("https://the-internet.herokuapp.com/windows")

a = driver.find_element(By.XPATH, "//*[@id='content']/div/a")
a.click()

#Eğer yeni bir sekme açıldı ise, seleniumun focusunun da o sekmeye aktarılması gerekir.
tabs = driver.window_handles
driver.switch_to.window(tabs[1])

h3 = driver.find_element(By.XPATH, "/html/body/div/h3")
print(h3.text)