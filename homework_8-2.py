def personal_sum(*args):
    result = 0
    incorrect_data = 0
    try:
        for i in args:
            result += i
    except TypeError:
        incorrect_data += 1
    print('result = ', result)
    print('incorrect_data = ', incorrect_data)
    return result

def calculate_average(*args):
    try:
        calc_ = personal_sum(*args) / len(*args)
    except ZeroDivisionError:
        calc_ = 0




personal_sum(1, 2, 'h', 4, 5, 8)
