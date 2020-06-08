"""
Создать квадратную матрицу размерностью n и заполнить ее случайными значениями от 1 до 9.
"""
import random

def create_matrix(a):
    matrix = []
    for i in range(a):
        matrix.append([])
        for j in range(a):
            matrix[i].append(random.randint(0, 9))

    for i in matrix:
        for j in i:
            print(j, end="\t")
        print("\n")

    return matrix


a = int(input('Введите р:азмер матрицы - '))

create_matrix(a)



