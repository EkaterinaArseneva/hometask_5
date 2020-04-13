"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
#opt 1 = работает и без построчного считыванрия
# replacements = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
# with open ('text_for_task_5_4.txt', encoding = 'utf8') as file_1:
#     content = file_1.read()
#
# for i, j in replacements.items():
#     content = content.replace(i, j)
#
# with open('replaced_values_for_task_5_3.txt', 'w', encoding='utf8') as file_2:
#     file_2.write(content)

#opt 2 = считываем построчно
replacements = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open ('text_for_task_5_4.txt', encoding = 'utf8') as file_1:
    for line in file_1:
        for i, j in replacements.items():
            if i in line:
                replaced_line = line.replace(i, j)
            else:
                continue
        with open('replaced_values_for_task_5_3.txt', 'a', encoding='utf8') as file_2:
            file_2.write(replaced_line)
