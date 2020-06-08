"""
Создать квадратную матрицу размерностью n и заполнить ее случайными значениями. Найти сумму всех элементов матрицы, которые кратны 3.
"""
import random


def create_matrix(a):
    matrix = []
    for i in range(a):
        matrix.append([])
        for j in range(a):
            matrix[i].append(random.randint(0, 20))

    for i in matrix:
        for j in i:
            print(j, end='\t')
        print()
    return matrix


def sum_el_matrix(matrix):
    sum = 0
    for i in matrix:
        for j in i:
            if j % 3 == 0:
                sum += j
    return sum

l = int(input('Введите размер матрицы - '))

print(f"Сумма элементов матрицы кратных 3 - {sum_el_matrix(create_matrix(l))}")