from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time 
driver = Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

alert_1_button = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[1]/button")
alert_1_button.click()
time.sleep(1)
alert = driver.switch_to.alert # alert'e focus olur. bir değişkene atar.
alert.accept() #Tamam
time.sleep(3)

alert2_button = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[2]/button")
alert2_button.click()
alert2 = driver.switch_to.alert
alert2.dismiss() # Cancel
time.sleep(3)

alert3_button = driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/button")
alert3_button.click()
alert3 = driver.switch_to.alert
alert3.send_keys("Deneme")
alert3.accept() # Cancel
time.sleep(3)