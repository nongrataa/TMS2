"""
Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором.
"""


def unique_number(list1, list2):
    list3 = []
    for i in list1:
        if i not in list2:
            list3.append(i)
    return list3


list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [1, 3, 5, 7, 9, 4, 99, 7]

print(unique_number(list1, list2))
