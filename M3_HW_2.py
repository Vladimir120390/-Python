def print_params(a=1, b='строка', c=True):
    print(a, b, c)
print_params()
print_params(10)
print_params(10, 'новая строка')
print_params(10, 'новая строка', False)
print()
print()
print_params(b = 25), print_params(c = [1,2,3])
print()
print()
values_list = [10, 'строка', False]
values_dict = {'a': 5, 'b': 'новая строка', 'c': [1, 2, 3]}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [7, 'другая строка']
print_params(*values_list_2, 42)


