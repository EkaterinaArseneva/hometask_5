"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

line = input('enter text: ')
with open("text.txt", 'w') as file:
    while line != "":
        file.write(line + '\n')
        line = input('enter text: ')
    print('text is written in file')

