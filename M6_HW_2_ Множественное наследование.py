class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"

class Car():
    def __init__(self):
        self.price = 1000000

    def horse_powers(self, engine_size):
        horse_powers = engine_size
        return horse_powers

class Nissan(Car, Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 1500000
        self.vehicle_type = "Nissan"

    def horse_powers(self, engine_size):
        horse_powers = engine_size * 1.25
        return horse_powers


nissan_car = Nissan()
engine_size = 100.0

print("Тип транспортного средства:", nissan_car.vehicle_type)
print("Цена автомобиля Nissan:", nissan_car.price)

