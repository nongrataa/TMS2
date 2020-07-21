"""Дан массив размерности (6,7,8). Каков индекс (x,y,z) сотого элемента?"""

import numpy as np

print(np.unravel_index(100, (6,7,8)))