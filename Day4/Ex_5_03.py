"""
Дан двумерный массив n × m элементов. Определить, сколько раз встречается число 7 среди элементов массива.
"""

import random


def create_matrix(n, m):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(random.randint(0, 9))

    for i in matrix:
        for j in i:
            print(j, end="\t")
        print()
    return matrix

def det_number(matrix):
    check = 0
    for i in matrix:
        for j in i:
            if j == 7:
                check += 1
    return check


a = int(input("Введите количество строк в матрице - "))
b = int(input("Введите количество столбцов в матрице - "))

print(f'Число 7 в матрице встречается {det_number(create_matrix(a, b))} раз.')

