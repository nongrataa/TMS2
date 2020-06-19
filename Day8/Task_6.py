"""Имеются два текстовых файла с одинаковым числом строк. Выяснить, совпадают ли их строки.
Если нет, то получить номер первой строки, в которой эти файлы отличаются друг от друга."""

with open('file6.txt') as my_file, open('file6_2.txt') as my_file2:
    f = my_file.readlines()
    f2 = my_file2.readlines()
    for i in range(len(f)):
        if f[i] == f2[i]:
            continue
        elif f[i] != f2[i]:
            print(f'{i+1} строка отличается')
            print(f'{f[i]} - {f2[i]}')
