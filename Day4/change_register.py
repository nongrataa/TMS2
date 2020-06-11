"""
Написать функцию, изменяющую регистр букв в слове так, чтобы оно либо состояло только из маленьких букв, либо, наоборот,
только из больших. При этом в слове должно измениться как можно меньше букв. Например, слово HoUse должно замениться на
house, а слово ViP — на VIP. В случае, если в слове содержится одинаковое количество маленьких и больших букв,
нужно заменить все буквы на маленькие. Например, maTRIx нужно заменить на matrix.
"""


def change_register(s):
    s = s.split(' ')
    new_string = ''
    for i in s:
        rsupper = 0
        rlower = 0
        for j in i:
            if j.isupper():
                rsupper += 1
            else:
                rlower += 1
        if rsupper > rlower:
            new_string += ' ' + i.upper()
        else:
            new_string += ' ' + i.lower()
    print('new_string -', new_string)
    return


string = 'ViP maxIM UNIq NuMbEr fsAJ jfeN HJdvJ fg'
change_register(string)
