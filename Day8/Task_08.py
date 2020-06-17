"""Имеется текстовый файл. Переписать в другой файл все его строки с
заменой в них символа 0 на символ 1 и наоборот."""


def rewrite_file(my_file, my_file2):
    f = my_file.readlines()
    new_f = []
    for i in f:
        for j in i:
            if j == '1':
                new_f.append('0')
            elif j == '0':
                new_f.append('1')
            else:
                new_f.append(j)

    my_file2.writelines(new_f)
    print()
    my_file2.close()
    my_file.close()


start_file = open('start.txt')
end_file = open('end.txt', 'w')

rewrite_file(start_file,end_file)