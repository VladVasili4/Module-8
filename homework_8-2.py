# result = 0
# length_ = 0
def personal_sum(numbers):
    global result
    global length_
    result = 0
    length_ = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
            length_ += 1
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')

    return (result, incorrect_data)

def calculate_average(numbers):
    try:
        res = personal_sum(numbers)
        average_ = res[0] / length_
        print(f'Среднее арифметическое :{average_}')
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
    return average_


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать