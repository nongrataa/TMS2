"""6. lambda, Дан список чисел. Найти произведение всех чисел, которые кратны 3."""
from functools import reduce

my_list = [3, 3, 4, 5, 6]
# g = reduce(lambda x, y: x * y if y % 3 == 0 else x, my_list, 1)
# print(g)

result = reduce(lambda x, y: x * y, filter(lambda x: x % 3 == 0, my_list))
print(result)
