import math
import numpy as np
x = 2
r = math.sin(x)*math.cos(x)*math.exp(-x**2) + 2 + x**2

print(r)

x = [1,2,4]

r = np.zeros(len(x))
for i in range(len(x)):
    r[i] = math.sin(x[i])*math.cos(x[i])*math.exp(-x[i]**2) + 2 + x[i]**2
    print(r)

