"""
1. Имеется текстовый файл. Напечатать:
a) его первую строку;
b) его пятую строку;
c) его первые 5 строк;
d) его строки с s1-й по s2-ю;
e) весь файл.
"""


def first_row(a):
    my_file = open(file)
    result = my_file.readline()
    my_file.close()
    return result


def fifth_row(a):
    i = 0
    with open(file) as my_file:
        for line in my_file.readlines():
            i += 1
            if i == 5:
                result = line
    my_file.close()
    return result


def first_fifth_lines(a):
    i = 0
    with open(file) as my_file:
        for line in my_file.readlines():
            i += 1
            print(line)
            if i == 5:
                break
    my_file.close()
    return


def between_lines(a, s1, s2):
    i = 0
    with open(file) as my_file:
        for line in my_file.readlines():
            i += 1
            if i >= s1:
                print(line)
            if i == s2:
                break
    my_file.close()
    return


def whole_file(file):
    my_file = open(file)
    while True:
        line = my_file.readline()
        if not line:
            break
        print(line)
    my_file.close()
    return


file = 'ffile.txt'

whole_file(file)
