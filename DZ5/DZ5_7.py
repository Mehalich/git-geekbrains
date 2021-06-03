"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json
firms = {}
positive_prof = []
f = open("DZ5_7.txt")
lines = f.readlines()
for line in lines:
    name, ownership, revenue, costs = line.split()
    profit = int(revenue) - int(costs)
    firms[name] = profit
    if profit > 0:
        positive_prof.append(profit)
average_prof = round(sum(positive_prof) / len(positive_prof), 2)
result = [firms, {"средняя прибыль:": average_prof}]
f.close()
with open("DZ5_7.json", "w") as f_json:
    json.dump(result, f_json)
with open("DZ5_7.json") as f_json:
    print(json.load(f_json))
