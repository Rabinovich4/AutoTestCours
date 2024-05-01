"""Фукция подсчёта гласных и согласных букв в строке"""


def counter_simbols(string_to_count):
    counter_vowels = 0
    counter_constants = 0
    for letters in string_to_count:
        if letters in "aeiouy":
            counter_vowels += 1
        elif letters in "bcdfghjklmnpqrstvwxz":
            counter_constants += 1
        elif letters == ' ':
            pass
        else:
            return print("Текст должен содержать только бквы английского алфавита")
    print(f'Кол-во гласных букв {counter_vowels}', f'Кол-во согласных букв {counter_constants}')


counter_simbols(input('Введите текст на английском языке: '))


"""Фукция переворта строки"""


def revers(string):
    new_string = ''
    for i in range(len(string) - 1, - 1, - 1):
        new_string += string[i]
    print(new_string)


revers(input('Введите текст для переворота: '))