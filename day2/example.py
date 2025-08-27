from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time 

def login_successfull():
    driver = Chrome() # Tarayıcı açtım
    driver.maximize_window() # Tam ekran yaptım
    waiter = WebDriverWait(driver, 10) # Alarm kurdum, beklediğim olay 10 saniyede gerçekleşmezse çalacak.
    driver.get("https://www.saucedemo.com/") # Websitesini açtım.
    # Websitesinde username_inputun gözükmesini bekle.
    username_input = waiter.until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))   
    #driver.find_element(By.ID, "user-name") #locate
    # Elemente tıkla ve yazı yaz.
    username_input.send_keys("standard_user")

    # Şifre inputu için aynılarını yap.
    waiter.until(expected_conditions.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
    # Butona tıkla
    waiter.until(expected_conditions.element_to_be_clickable((By.ID, "login-button"))).click()

    # Assertion -> ileride değişecek.
    print(driver.current_url == "https://www.saucedemo.com/inventory.html")
    # Tarayıcı kapat.
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

# Sepete ürün ekleme testi.
# Giriş yap -> Add To Cart butonuna tıklama -> Sağ üstteki sepet ikonunda 1 yazısının doğrulanması.
def add_item_to_cart():
    driver = Chrome() 
    driver.maximize_window()
    waiter = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")
    username_input = waiter.until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))   
    username_input.send_keys("standard_user")
    waiter.until(expected_conditions.visibility_of_element_located((By.ID,"password"))).send_keys("secret_sauce")
    waiter.until(expected_conditions.element_to_be_clickable((By.ID, "login-button"))).click()
    waiter.until(expected_conditions.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
    #cart_badge = waiter.until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='shopping_cart_container']/a/span")))
    cart_badge = waiter.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='shopping-cart-badge']")))
    print("Kart ürün sayı göstergesi: "+cart_badge.text)


# Bütün ürünlerin listesi alınıp
# Fiyat değerinin boş olmadığı ve $ ile başladığı.
def price_format_test():
    pass

#Giriş yap -> Hamburger menüyü aç -> Çıkış yap -> URL'in giriş sayfasına döndüğünü doğrula.
def logout():
    pass



add_item_to_cart()
time.sleep(30)


# presence_of_element_located -> Element DOM ağacında var mı?
# visibility_of_element_located -> Element DOM ağacında var mı ve görünür mü?
# element_to_be_clickable -> Element DOM ağacında var mı, görünür mü ve tıklanabilir mi?
# text_to_be_present_in_element -> Elementin içinde spesifik bir yazı görünene kadar.
# alert_is_present -> Tarayıcı bir alert çıkarana kadar bekler.