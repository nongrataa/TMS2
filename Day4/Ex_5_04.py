"""
Дана целочисленная матрица А[n,m].
Посчитать количество элементов матрицы, превосходящих среднее арифметическое значение элементов матрицы и сумма индексов которых четна.[02-4.2-BL23]
"""
import random


def create_matrix(n, m):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(random.randint(0, 10))

    for i in matrix:
        for j in i:
            print(j, end='\t')
        print()
    return matrix


def average_matrix(matrix):
    average = 0
    count = 0
    sum = 0
    for i in matrix:
        for j in i:
            count += 1
            sum += j
    average = sum / count
    return average


def count_el_matrix(matrix, average):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > average and (i + j) % 2 == 0:
                count += 1
                print(f'i - {i} j - {j} el - {matrix[i][j]}')
    return count


_matrix = create_matrix(3, 3)
_average = average_matrix(_matrix)
print(f'average matrix - {_average}')
_count = count_el_matrix(_matrix, _average)
print(f"Count - {_count}")
