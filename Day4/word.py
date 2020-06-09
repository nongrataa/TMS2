"""
Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.
"""


def max_len_word(string):
    string = string.split(' ')
    dict_len = {}
    max_el = 0
    key_el = ''
    for i in string:
        s_len = 0
        for j in i:
            s_len += 1
            dict_len[i] = s_len
        for key, value in dict_len.items():
            if max_el < value:
                max_el = value
                key_el = key
    return key_el


def max_word(string):
    string = string.split(' ')
    dict = {}
    max_el = 0
    key_el = ''
    for i in string:
        print('dict - ', dict)
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    for key, value in dict.items():
        if max_el < value:
            max_el = value
            key_el = key
    return key_el


string = 'qwerty asssdfg zxcv qwerty zxcv zxcv df sdf zxcv zxcv sdf'

print(max_word(string))
print(max_len_word(string))
