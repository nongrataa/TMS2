def change_before_diagana(matrix_a, matrix_b):
    index = 0
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[i])):
            if i > index and j <= index + 1:
                matrix_a[i][j], matrix_b[i][j] = matrix_b[i][j], matrix_a[i][j]
            if i <= index and j >= index + 1:
                print(matrix_a[i][j])
                matrix_a[i][j], matrix_b[i][j] = matrix_b[i][j], matrix_a[i][j]

    return matrix_b


a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 2]
]
b = [
    [5, 6, 2],
    [1, 7, 4],
    [9, 3, 7]
]

print(change_before_diagana(a, b))
