"""cоздать массив 10x10 со случайными значениями, найти минимум и максимум"""
import math
import numpy as np

a = np.random.random((10,10))
print(a)

amin = a.min()
amax = a.max()

print('amin',amin)
print('amax',amax)