def add_everything_up(a, b):
    try:
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = a + b
            if isinstance(a, (int, float)):
                result = truncate_number(result)
            return result
        else:
            raise TypeError
    except TypeError:
        return str(a) + str(b)

def truncate_number(num):
    num_str = str(num)
    if '.' in num_str:
        integer_part, decimal_part = num_str.split('.')
        truncated_decimal_part = decimal_part[:3]
        truncated_num = float(f"{integer_part}.{truncated_decimal_part}")
        return truncated_num
    else:
        return num

# Пример использования функции add_everything_up
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

