"""
Создать список с фамилиями. Вывести все фамилии, которые начинаются на П и заканчиваются на а
"""

surname = ['Сандакова', 'Петрашка', 'Кийко', 'Петрова', 'Дворецкий']

for i in surname:
    if i[0] == 'П' and i[-1] == 'а':
        print(i)
