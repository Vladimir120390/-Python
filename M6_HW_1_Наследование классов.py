class Car:
    def __init__(self):
        self.price = 1000000
    def horse_powers(self, engine_size):
        # Предположим, что для простоты расчета мы используем формулу engine_size * 0.1
        horse_powers = engine_size
        return horse_powers

class Nissan(Car):
    def __init__(self):
        super().__init__()
        self.price = 1500000

    def horse_powers(self, engine_size):
        horse_powers = engine_size * 1.25
        return horse_powers

class Kia(Car):
    def __init__(self):
        super().__init__()
        self.price = 500000

    def horse_powers(self, engine_size):
        horse_powers = engine_size * 0.8
        return horse_powers

my_car = Car()
nissan_car = Nissan()
kia_car = Kia()
engine_size = 200.0

print()
print("Цена автомобиля Car:", my_car.price)
print("Лошадиные силы автомобиля Car:", my_car.horse_powers(engine_size))
print()
print("Цена автомобиля Nissan:", nissan_car.price)
print("Лошадиные силы автомобиля Nissan:", nissan_car.horse_powers(engine_size))
print()
print("Цена автомобиля Kia:", kia_car.price)
print("Лошадиные силы автомобиля Kia:", kia_car.horse_powers(engine_size))


