class Car(): # sisteme yeni bi obje tanıttım.
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        print("abc123")

    def start_rent(self): 
        # self parametresi classın kendisini temsil eder. fonk. class seviyesine ulaşım sağlar
        print(f"{self.brand} marka {self.model} modelindeki araç kiralaması başlatılıyor.")
        #print(self.color + " rengindeki araç." + self.year + " yıl modeli.")
        self.example()
    def example(self):
        print("Example çağırıldı.")

# Eğer kalıtım varsa
# Kalıtım alınan classa (Car) superclass
# Kalıtım alan classa (ElectricCar) subclass denir.
class ElectricCar(Car): #Car'daki bütün özellikler bu classda da vardır.
    def __init__(self, brand, model, year, color, battery):
        super().__init__(brand, model, year, color)
        self.battery = battery
        
    def charge(self):
        print("Araç şarj ediliyor..")

# instance - örnek
car1 = Car("Toyota","Corolla",2025, "Kırmızı") # ilgili nesneden yeni bir üretim yaptım.
print(car1.year) # get
car1.start_rent() # fonk.

car2 = Car("Fiat","Egea",2024,"Beyaz") # nesneyi üretmek -> nesnenin __init__() çağırmak demek
print(car2.year)
car2.start_rent()
