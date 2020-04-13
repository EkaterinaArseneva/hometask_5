"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
my_dict = {}
with open('text_for_task_5_3.txt') as file:
    content = file.readlines()
    for line in content:
        name, salary = line.split()
        my_dict.update({name: float(salary)})


underpaid = [name for name in my_dict if my_dict[name] < 20000]
print(f'{underpaid} get salaries lower 20000')

average_salary = round(sum(my_dict.values())/len(my_dict), 2)
print(f'average salary is {average_salary}')