def test(a, b):
    print(a, b)
test(1,2)
print()# для лучшей читаемости))


def test2(a, *, b=True, c=1):# вариант № 1
    print(a,b,c)
test2(a="OK")
print()# для лучшей читаемости))


name = input("Введите имя: ") # вариант № 2
lastname = input("Введите фамилию: ")
age = int(input("Введите Ваш возраст: "))
def test2(name, lastname,age):
            print(name, lastname, age)
test2(name, lastname, age)





