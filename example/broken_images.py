from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time 
from requests import get

driver = Chrome()
driver.get("https://the-internet.herokuapp.com/broken_images")

images = driver.find_elements(By.TAG_NAME, "img")

broken_images = []
for image in images:
    response = get(image.get_attribute("src"))
    if response.status_code != 200:
        broken_images.append(image.get_attribute("src"))

print("Bozuk imagelar:", broken_images)