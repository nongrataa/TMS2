"""Имеется текстовый файл. Все четные строки этого файла записать во второй файл, а нечетные — в третий файл.
Порядок следования строк сохраняется."""

with open('file5.txt') as my_file_open, open('file5_2.txt', 'w') as my_file_save, open('file5_3.txt',
                                                                                       'w') as my_file2_save:
    f = my_file_open.readlines()
    for i in range(len(f)):
        if (i + 1) % 2 == 0:
            my_file_save.write(f[i])
        else:
            my_file2_save.write(f[i])
