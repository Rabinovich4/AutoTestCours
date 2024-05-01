"""Определение Времени Года"""
def seasons(month_num):
    if 1 <= month_num <= 12:
        if month_num in [12, 1, 2]:
            print("Зима")
        elif month_num in [3, 4, 5]:
            print("Весна")
        elif month_num in [6, 7, 8]:
            print("Лето")
        else:
            print("Осень")
    else:
        print("В году 12 месяцев, введите число от 1 до 12")


print('Введите номер месяца')
seasons(int(input()))


"""Ранг Пользователя"""


def user_rang(points):
    if 1 <= points <= 999:
        print("Новичок")
    elif 1000 <= points <= 4999:
        print("Любитель")
    elif points >= 5000:
        print("Мастер")


print('Введите кол-во очков')
user_rang(int(input()))


"""Скидка на покупку"""


def discount(bill):
    if 1000 <= bill <= 2000:
        print(bill - (bill / 100 * 5))
    elif bill >= 2001:
        print(bill - (bill / 100 * 10))
    else:
        print('Скидка не продоставляется')


print('Введите сумму покупок')
discount(int(input()))


"""Вывод чётных чисел"""

print('Введите число для подсчёта чётных чисел')
user_num = int(input())

for i in range(1, user_num + 1):
    if i % 2 == 0:
        print(f'Чётная {i}')


"""Подсчёт кол-ва цифр"""

print('Введите число для подсчёта суммы цифр')
user_digit = int(input())

counter = 0
for c in str(user_digit):
    counter += 1
print(f'Кол-во цифр с числе {counter}')


"""Подсчёт кол-ва цифр"""

print('Введите строку чисел разделённых пробелом для подсчёта суммы чисел')
user_string = input().split()

summ = 0
for c in user_string:
    summ += int(c)
print(f'Сумма чисел в строке {summ}')
