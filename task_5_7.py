"""Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

dict_firms = {}
average_profit = []
with open('text_for_task_5_7.txt', encoding='utf8') as file:
    for line in file:
        line = line.split()
        name = line[0]
        profit = int(line[2]) - int(line[3])
        dict_firms.update({name: profit})
        if profit > 0:
            average_profit.append(profit)
average_profit = sum(average_profit)/len(average_profit)
aver_profit_dict = {'average_profit': average_profit}
final_list = [dict_firms, aver_profit_dict]

with open("task_5_7.json", "w") as write_f:
    json.dump(final_list, write_f)