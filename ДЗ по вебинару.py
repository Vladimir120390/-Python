n = int(input("Введите положительное, целое число: "))   #Задача на For#1
for i in range(n, 0, -1):
    print('*' * i)
print()


a, b, c, d = map(int, input("Введите четыре целых числа от 1 до 10: ").split())     #Задача на For#2
print('\t', end='')
for i in range(c, d + 1):
    print(i, end='\t')
print()
for i in range(a, b + 1):
    print(i, end='\t')
    for j in range(c, d + 1):
        print(i * j, end='\t')
    print()
    print()


n = int(input("Введите положительное, целое число: "))   #Задача на For#3
current_number = 1
for i in range(1, n+1):
    for j in range(i):
        print(current_number, end=' ')
        current_number += 1
    print()
print()


a, b, c = map(int, input("Введите три целых числа: ").split())     #Задача на If#1
if a == b == c:
    result = "Равносторонний"
elif a == b or a == c or b == c:
    result = "Равнобедренный"
else:
    result = "Разносторонний"
print("result —>", result)
print()


a, b, c = map(int, input("Введите три целых числа: ").split())   #Задача на If#2
if (a <= b <= c) or (c <= b <= a):
    result = b
elif (b <= a <= c) or (c <= a <= b):
    result = a
else:
    result = c
print("result —>", result)
print()


a = input("Введите первый основной цвет (красный, синий, желтый): ")    #Задача на If#3
b = input("Введите второй основной цвет (красный, синий, желтый): ")
if (a == "красный" and b == "синий") or (a == "синий" and b == "красный"):
    result = "фиолетовый"
elif (a == "красный" and b == "желтый") or (a == "желтый" and b == "красный"):
    result = "оранжевый"
elif (a == "синий" and b == "желтый") or (a == "желтый" and b == "синий"):
    result = "зеленый"
else:
    result = "Ошибка: введите корректные названия цветов (красный, синий, желтый)"
print("result —>", result)
