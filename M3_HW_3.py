def test_(*args):
    for arg in args:
        print(arg)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

test_(1, "hello", [1, 2, 3], True)
result = factorial(5)
print("Факториал числа 5 равен:", result)


