# bir py dosyasında diğer dosya/kütüphanelerden alınan referanslar
# 1- Built-in modüller
#import math
from math import sqrt
import os
# 2- Kendi yazdığımız dosyalar.
from functions import connect_database
# 3- pip ile kurulan 3rd party libraryler.
import requests
#from requests import get

print(sqrt(25))
os.makedirs("example",exist_ok=True)
connect_database("v3")

response = requests.get("https://google.com.tr")
print(response)