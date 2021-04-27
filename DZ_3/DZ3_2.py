"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Реализовать вывод данных
о пользователе одной строкой.
"""


def data_user(name, l_name, b_date, l_town, email, phone):
    return f"{name}, {l_name}, {b_date}, {l_town}, {email}, {phone}"


print(data_user(name="Uasya", l_name="Pupkin", b_date=2000, l_town="Tirana", email="u_pupkin@udaff.com", phone="+7987654321"))
