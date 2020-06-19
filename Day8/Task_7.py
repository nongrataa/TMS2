"""Создать матрицу случайных чисел и сохранить ее в json файл.
После прочесть ее, обнулить все четные элементы и сохранить в другой файл"""

import random
import json

matrix = []

for i in range(0, 4):
    matrix.append([])
    for j in range(0, 4):
        matrix[i].append(random.randint(0, 10))
print('matrix - ', matrix)

with open('file7.json', 'w') as my_file_save:
    json.dump(matrix, my_file_save)

with open('file7.json') as my_file_load:
    f = json.load(my_file_load)
    print(f)
    for i in range(len(f)):
        for j in range(len(f[i])):
            if j % 2 == 0:
                f[i][j] = 0
    print(f)

with open('file7_2.json', 'w') as my_file2_save:
    json.dump(f, my_file2_save)

