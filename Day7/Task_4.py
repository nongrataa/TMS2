"""lambda, Дан список чисел. Вернуть список, где каждый число переведено в строку
[5, 3] -> [‘5’, ‘3’]"""

my_list = [1, 2, 3, 4, 5, 6, 7]
print(list(map(lambda x: str(x), my_list)))