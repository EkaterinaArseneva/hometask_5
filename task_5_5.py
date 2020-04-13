"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

with open ('text_for_task_5_5.txt', 'w+') as file:
    try:
        numbers = input('enter numbers with space sep: ')
        file.write(numbers)

        file.seek(0)
        numbers_list = list(map(float, file.read().split()))
        numbers_sum = sum(numbers_list)
        print(f'sum of numbers is: {numbers_sum}')

    except ValueError:
        print('ensure you enter numbers and use space as separator')