from scipy import integrate
import numpy as np

n = 5
def f(t, x):
    return np.exp(-x*t)/t**n


a = 2
b = 1
res = integrate.nquad(f, [[1, np.inf], [0, np.inf]])

print(res)