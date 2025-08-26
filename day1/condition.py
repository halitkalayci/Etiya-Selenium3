# Operatörler

# Aritmetik Operatörler
print(25+25)
print(25-5)
print(25*3)
print(25/3) #ondalıklı (float,double)
print(25//3) #tam böl (int) 
print(100%3) #mod
#(eğer tam bölünmüyor ise aşağıya yuvarlar.)

# Karşılaştırma Op.
# bool,Boolean => True False
print(5 == 5) #sol taraf ve sağ taraf birbirine eşit mi?
print(5 == 6)
print(5 != 3) # eşit olmasınlar.

print(10 > 5) # numerik ifade
print(10 < 5)
print(10 >= 10)
print(10 <= 10)
print("Merhaba" == "merhaba")
#

# Scope kavramı #
# Kapsam-Blok
# Boşluk (Indentation)
if 5 < 3:
    print("Durum sağlandı.") # tab -> bir indentation içeri
    print("İF içerisindeyim") # shift+tab -> bir indentation dışarı
print("İF dışarısı")
#
# "" -> Metinsel ifade

# Karar-Şart blokları.
print(10) #numerik
print("10") #metinsel


age = 18

# Her blok yalnızca 1 karar çıkartır.
# Yukarıdan aşağıya doğru (True) olan ilk karar.

if age >= 18: # 1. koşul
    print("Kullanıcı reşit")
elif age == 18: # 2. koşul
    print("Kullanıcı tam 18, ay kontrolü yapılıyor.")
else: # hiç bir koşul sağlanmıyor
    print("Kullanıcı reşit değil")

# if -> bir koşul belirler 
# elseif (elif) -> üstündeki koşul sağlanmıyorsa yeni bi koşul test eder.
# else -> hiç bir if,elif çalışmadıysa çalışır.

# ve -> True-True dışında hep false döner.
print(10 == 10 and 5 == 3) #and -> iki koşulu "ve" mantığında bağlar.
print(10 == 10 and 5 == 5)

# veya -> False-False dışında hep true döner.
print(10 == 10 or 5 == 3) #or -> iki koşulu "veya" mantığında bağlar.
print(10 == 10 or 5 == 5)

username = input("Kullanıcı adı: ")
password = input("Şifre: ")

if username == "halit" and password == "123":
    print("Giriş başarılı")
else:
    print("Giriş başarısız.")

gecikmisFatura = False
taahutSonu = True

if gecikmisFatura or taahutSonu:
    print("Kullanıcıya sms gönderiliyor")
else:
    print("Herhangi bir hatırlatma yok.")

