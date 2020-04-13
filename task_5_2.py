"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""
with open('text_for_task_5_2.txt') as text_file:
    lines = text_file.readlines()
    rows_count = len(lines)
    print(f'your text has {rows_count} rows')
    for index, line in enumerate(lines,1):
        words_count = len(line.split())
        print(f'{index} row has {words_count} words')
