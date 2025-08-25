# entrypoint

students = ["Halit","Semih","Köksal","İkbal"]

print(students[0])

# Bir bloğun bir kere değil N kere çalıştırılması.

# Döngüler -> belirlenen durum kadar aynı kodun "iterate" edilmesi.
for i in range(10): #range->0dan verdiğim sayıya kadar (dahil olmamak üzere) iterasyon oluştur.
    print(i)

for i in range(5,10):
    print(i)

for student in students:
    if student == "Semih":
        #continue # Bu iterasyonu atla, sonraki iterasyonla devam et.
        break # Döngüyü tamamen sonlandır.
    print("Öğrenci: " + student)


# while -> veri üzerinde değil şart üzerinde çalışır.
# şart döngü içinde değişmiyorsa sonsuz döngü yaratılır.
a = 5
while a < 10:
    a += 1 # a'yı bir artır.
    print("Merhaba")

