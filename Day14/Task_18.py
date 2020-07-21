"""Перемножить матрицы 5x3 и 3x2"""

import numpy as np

a = np.ones((5,3))
b = np.ones((3,2))
print(a)
print(b)

print(a.dot(b))