"""
3. Реализовать функцию my_func(), которая принимает три
позиционных аргумента, и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    my_list.sort(reverse=True)
    return my_list[0] + my_list[1]


print(my_func(7, 4, 6))
