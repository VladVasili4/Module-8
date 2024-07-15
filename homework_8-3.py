class IncorrectVinNumber(Exception):
    def __init__(self, message):
        pass

    # print('Некорректный тип vin номер')


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        pass


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, float):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        return True


    def __is_valid_numbers(numbers):
        pass

car1 = Car('Mod1', 5555555, 'r222op')
print(car1._Car__is_valid_vin(55))