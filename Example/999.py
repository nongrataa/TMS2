a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 2]
]

max_element = 0

for i in a:
    for j in range(len(i)):
        if j == 1 and max_element < i[j]:
            max_element = i[j]

print(max_element)

#
# def max_matrix(a, b):
#     """
#     :param a: matrix
#     :type: list
#     :param b: number
#     :type: int
#     :return:
#     :type: int
#     """
#
#     if b-1 >= len(a[1]):
#         return print("False")
#
#     max_element = 0
#     for i in a:
#         for j in range(len(i)):
#             if j == b - 1 and max_element < i[j]:
#                 max_element = i[j]
#
#     return max_element
#
#
# c = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 2]
# ]
#
# print(max_matrix(c,4))



#
# def max_matrix(a, b, s):
#     """
#     :param a: matrix
#     :type: list
#     :param b: number
#     :type: int
#     :param s: number
#     :type: int
#     :return:
#     :type: int
#     """
#
#     for i in a:
#         for j in range(len(i)):
#             if i[j] == b:
#                 i[j] = s
#
#     return a
#
#
# c = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 2]
# ]
#
# print(max_matrix(c, 8, 100))

#
# def max_matrix(a, b, s):
#     """
#     :param a: matrix
#     :type: list
#     :param b: number
#     :type: int
#     :param s: number
#     :type: int
#     :return:
#     :type: int
#     """
#
#     for i in a:
#         for j in range(len(i)):
#             if i[j] == b:
#                 i[j] = s
#
#     return a
#
#
# c = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 2]
# ]
#
# print(max_matrix(c, 8, 100))
#
# matrix = max_matrix(c, 8, 100)
#
# for i in matrix:
#     for j in i:
#         print(j, end="\t")
#     print("\n")

# def max_matrix(a):
#     """
#     :param a: matrix
#     :type: list
#     :param b: number
#     :type: int
#     :param s: number
#     :type: int
#     :return:
#     :type: int
#     """
#     g = len(a[1]) - 1
#     h = 0
#     print(g)
#
#     for i in a:
#         for j in range(len(i)):
#             if j == g:
#                 i[j] = 0
#                 g -= 1
#
#             if j == h:
#                 i[j] = 1
#         h += 1
#
#     return a
#
#
# c = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 2]
# ]
#
# matrix = max_matrix(c)
#
# for i in matrix:
#     for j in i:
#         print(j, end="\t")
#     print("\n")
