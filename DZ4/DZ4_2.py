import random

"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
task_list = []
result_list = []
for step in range(0, 100):
    task_list.append(random.randint(0, 1000))
for step in range(1, len(task_list)-1):
    if task_list[step+1] > task_list[step]:
        result_list.append(task_list[step+1])
print(task_list)
print(result_list)
