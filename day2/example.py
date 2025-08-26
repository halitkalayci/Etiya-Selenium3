from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time 

def login_successfull():
    driver = Chrome()
    driver.maximize_window()
    waiter = WebDriverWait(driver, 10) 
    driver.get("https://www.saucedemo.com/")
    username_input = waiter.until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))     #driver.find_element(By.ID, "user-name") #locate
    username_input.send_keys("standard_user")

    waiter.until(expected_conditions.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")

    waiter.until(expected_conditions.element_to_be_clickable((By.ID, "login-button"))).click()
    print(driver.current_url == "https://www.saucedemo.com/inventory.html")
    driver.quit()

def login_unsuccessful():
    driver = Chrome()
    driver.maximize_window()
    waiter = WebDriverWait(driver, 10) 
    driver.get("https://www.saucedemo.com/")
    username_input = waiter.until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))     #driver.find_element(By.ID, "user-name") #locate
    username_input.send_keys("standard_user")

    waiter.until(expected_conditions.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce123")

    waiter.until(expected_conditions.element_to_be_clickable((By.ID, "login-button"))).click()
    error_h3 = waiter.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")))
    print(error_h3.text == "Epic sadface: Username and password do not match any user in this service")
    driver.quit()


login_successfull()
login_unsuccessful()
time.sleep(30)


# presence_of_element_located -> Element DOM ağacında var mı?
# visibility_of_element_located -> Element DOM ağacında var mı ve görünür mü?
# element_to_be_clickable -> Element DOM ağacında var mı, görünür mü ve tıklanabilir mi?
# text_to_be_present_in_element -> Elementin içinde spesifik bir yazı görünene kadar.
# alert_is_present -> Tarayıcı bir alert çıkarana kadar bekler.