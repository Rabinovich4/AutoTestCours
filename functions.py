"""Фукция перевода градусов цельсия в градусы по фаренгейту (дубль из variables_and_data_types я там случайно уже так сделал)"""


def convert_temperature(temperature_to_convert):
    save_temperature = temperature_to_convert
    print(f'Температура по фаренгейту {(save_temperature * 9) / 5 + 32}')


convert_temperature(int(input('Введите температуру в градусах цельсия: ')))


"""Факториал"""


def factorial(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    print(f"Факториал числа {n} равен {factorial}.")


factorial(int(input('Введите число для подсчёта факториала: ')))