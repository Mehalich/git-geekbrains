"""
Урок 3. Функции
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.
"""


def my_sep(arg_1, arg_2):
    if arg_2 == 0:
        return "Деление на ноль невозможно!"
    return arg_1 / arg_2


num_1 = int(input("Введите делимое: "))
num_2 = int(input("Введите делитель: "))
print(my_sep(num_1, num_2))
