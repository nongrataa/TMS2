
def write_file(file, string):
    with open(file, 'w') as my_file:
        for line in string:
            my_file.write(line + '\n')
    return


def enter_string():
    my_list = []
    for i in range(0, 6):
        string = str(input(f'Введите строку - {i+1} - '))
        my_list.append(string)
    write_file(file, my_list)


file = 'test.txt'
enter_string()