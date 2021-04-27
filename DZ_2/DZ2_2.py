"""
2. Для списка реализовать обмен значений соседних элементов,
т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

various_list = []
max_steps = 5
step = 0
while step != max_steps:
    various_list.append(input(f"Введите {step+1}-е значение списка: "))
    step += 1
print(f"Ваш список : {various_list}")

step = 1
max_steps = len(various_list)
if max_steps / 2 != 0:
    max_steps -= 1
while step <= max_steps:
    various_list.insert(step-1, various_list[step])
    various_list.pop(step+1)
    step += 2
print(f"Ваш список после магии : {various_list}")
