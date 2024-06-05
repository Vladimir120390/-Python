class Building:
    total = 0

    def __init__(self):
        Building.total += 1

# Создание 40 объектов класса Building
for i in range(40):
    building = Building()

print(Building.total)  # Вывод количества созданных объектов
