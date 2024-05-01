"""Задание 1"""

age = 18
height = 189.3
name = "Kirill"
numbers = [1, 2, 3, 4, 5]
colors = ("red", "green", "blue")
person = {"name": "Edvard", "age": 35, "city": "Moscow"}

print("Сумма возраста и роста:", age + height)

full_name = f'{name} {person.get("name")}'
print("Полное имя:", full_name)

numbers.append(6)
print("Список чисел с добавленным 6:", numbers)

print("Второй цвет из кортежа:", colors[1])

person.pop("city")
print("Измененный словарь без ключа 'city':", person)


"""Задание 2 name и age взяты из Задание 1"""

temperature = 25.5
is_student = True
print(type(name), type(age), type(temperature), type(is_student))
print(f"Hello, my name is {name}. I am {age} years old. Today's temperature is {temperature}°C. Am I a student? {is_student}.")

"""Задания для самостоятельного решения"""


def convert_temperature(temperature_to_convert):
    save_temperature = temperature_to_convert
    print(f'Температура по фаренгейту {(save_temperature * 9) / 5 + 32}')


convert_temperature(5)


def average(num_1, num_2, num_3):
    print(f'Среднеарифметическое значение {(num_1 + num_2 + num_3) / 3}')


average(7, 4, 3)


def even_not_even(num):
    if num % 2 == 0:
        print(f"Число {num} чётное")
    else:
        print(f"Число {num} не чётное")


even_not_even(6)