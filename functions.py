print("Fonksiyonlar.")


# 15-20 satır

# Fonksiyonlar -> Kodun tekrar kullanılabilirliğini yükseltmek ve bakım maliyetini azaltmak

# Args-Parametreler
# Return
# Modules
def connect_database(db_name):
    print(db_name+" veritabanına bağlanma kodu çalıştırılıyor..")
    print("Satır 1")
    print("Satır 2")
    print("Satır 3")
    print("Satır 4")

def toplama(a,b):
    #print(a+b)
    result = a + b
    return result
# Varsayılan argüman (default arg.)
def selamla(name="kullanıcı"):
    print("Merhaba, " + name)

selamla()
selamla("Halit")

connect_database("v1")
connect_database("v2")

a = toplama(3,5)
b = toplama(1,5)

print(a)
print(b+50)