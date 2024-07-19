def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        try:
            result = func(int_list)
            results[func.__name__] = result
        except Exception as e:
            results[func.__name__] = f'Error: {str(e)}'
    return results

def custom_min(int_list):
    return min(int_list)

def custom_max(int_list):
    return max(int_list)

def custom_len(int_list):
    return len(int_list)

def custom_sum(int_list):
    return sum(int_list)

def custom_sorted(int_list):
    return sorted(int_list)

print(apply_all_func([6, 20, 15, 9], custom_max, custom_min))
print(apply_all_func([6, 20, 15, 9], custom_len, custom_sum, custom_sorted))
