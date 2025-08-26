class Car(): # sisteme yeni bi obje tanıttım.
    brand = ""
    model = ""
    year = 0
    color = ""

    def start_rent(self): 
        # self parametresi classın kendisini temsil eder. fonk. class seviyesine ulaşım sağlar
        print(self.brand + " marka aracın kiralaması başlatılıyor.")


# instance - örnek
car1 = Car() # ilgili nesneden yeni bir üretim yaptım.
car1.brand = "Toyota" # set
car1.model = "Corolla" # set
car1.color = "Kırmızı" # set
car1.year = 2025 # set
print(car1.year) # get
car1.start_rent()