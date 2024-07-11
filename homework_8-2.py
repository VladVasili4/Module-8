result = 0
def personal_sum(*args):
    global result
    incorrect_data = 0
    for i in args:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    print('result = ', result)

    return (result, incorrect_data)



def calculate_average(*args):
    try:
        length_ = len(args)
        print(length_)
    except:
    res = personal_sum(*args)
    average_ = res[0] / length_
    print(f'Среднее арифметическое :{average_}')
    # except TypeError:
    #     print(f'Некорректный тип данных для подсчёта суммы')
    #
    # print(average_)
    #
    # try:
    #     # calc_ = res / length_
    #     calc_ = res/ length_
    # except ZeroDivisionError:
    #     calc_ = 0
    # return calc_



# print(personal_sum(1, 'h', 4, 5, 8))
print(f'Результат 0: {calculate_average(1, 14, 4, 5, 8)}')

# print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
# print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
# print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
# print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать