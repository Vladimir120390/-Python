def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    try:
        for num in numbers:
            if isinstance(num, (int, float)):
                result += num
            else:
                print(f'Некорректный тип данных для подсчёта суммы - {num}')
                incorrect_data += 1
    except TypeError:
        incorrect_data += 1

    return result, incorrect_data


def calculate_average(numbers):
    try:
        result, incorrect_data = personal_sum(numbers)
        if len(numbers) == 0:
            return 0
        else:
            return result / len(numbers)
    except ZeroDivisionError:
        return 0
    except TypeError:
        return None


# Примеры вызова функции calculate_average
result1, incorrect_data1 = personal_sum("1, 2, 3")
print(f'Результат 1: {result1}')
result2, incorrect_data2 = personal_sum([1, "Строка", 1.0, "Ещё Строка"])
print(f'Результат 2: {result2}')
print(f'В numbers записан некорректный тип данных')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
