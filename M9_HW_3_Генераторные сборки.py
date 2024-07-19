first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Первая часть задачи
first_result = (len(s1) - len(s2) for s1, s2 in zip(first, second) if len(s1) != len(s2))

# Вторая часть задачи
second_result = (first[i] == second[i] for i in range(min(len(first), len(second))))

# Вывод результатов
print(list(first_result))
print(list(second_result))





