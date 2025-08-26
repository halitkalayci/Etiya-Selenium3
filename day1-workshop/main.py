# veriyi verecek
import bank
# verinin serüvenini kodla.

inp = input("Yapılacak işlemi seçiniz. \n 1. Kayıt Ol \n 2. Giriş Yap \n Q. Çıkış")

while inp != "Q":
    if inp == "1":
        username = input("Kullanıcı adı giriniz: ")
        password = input("Şifre giriniz: ")
        bank.register(username, password)
    elif inp == "2":
        username = input("Kullanıcı adı giriniz: ")
        password = input("Şifre giriniz: ")
        bank.register(username, password)
    elif inp == "3":
        pass # .....
    inp = input("Yapılacak işlemi seçiniz. \n 1. Kayıt Ol \n 2. Giriş Yap \n Q. Çıkış")
    

print("Program sonlandı.")
