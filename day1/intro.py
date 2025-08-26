print("Merhaba")

# Bu bir yorum satırıdır.

# Değişkenler -> İsim ile bir veri tutmak ve bu verinin
# değişebilir olması.
a = 5 #integer -> tam sayı
print(a) # ram'e git, a'nın değeri kaçsa bunu bana getir.
print(5)

a = 10
print(a)
print( type(a) )
#
a = "Halit" # string -> metinsel
print(a)

# Python type-safe değildir.
print( type(a) )

# Değişken isim kuralları.
# Sayı ile başlayamaz, sayı içerebilir.
# Türkçe karakter kullanılması önerilmez.
# - *
a2 = "Merhaba"
# Wildcard (Semboller) programlamada anlamlı olduğu için
# içeremez.
#a* = 5
#print(a*)
# Büyük-küçük harf duyarlıdır age-Age farklı 2 değişkendir.
age = 50
print(age)


b, c, d = 10, 20, 30
print(b,c,d)

x = y = z = 0
print(x,y,z)

student1 = "Halit"
student2 = "Engin"

# list -> Sıralı, değiştirilebilir koleksiyon.
students = ["Halit","Engin","Ecem","Emre"]
print(students[0]) # index numarası
print(students[1]) # get
students[1] = "Enes" # set
print(students[1])

students.append("Yusuf") #Built-in
print(students)

# tuple -> Sıralı ama değiştirilemez koleksiyon
numbers = (10,20,30)
print(numbers[1]) # get
#numbers.append(40)
#numbers[1] = 40
istanbul = (41,28)


students.remove("Ecem")
print(students)

students.pop(0) # Varsayılan olarak son indexdeki elemanı siler
# ancak spesifik index belirebiliriz.
print(students)


# dict -> json'a benzer
# index mantığı key mantığına dönüşüyor.
# key-value
person = {
    "name":"Halit Enes",
    "surname":"Kalaycı",
    "age":26
}
print(person["age"])
person["age"] = 30
print(person["age"])










