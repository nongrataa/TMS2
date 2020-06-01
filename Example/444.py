# Решение квадратного уравнения
#
import math

a = int(input("input a -  "))
b = int(input("input b -  "))
c = int(input("input c -  "))
x1 = 0
x2 = 0
d = (b ** 2) - (4 * a * c)

if d == 0:
    x1 = -b / 2 * a
    print("x1 = ", x1)
elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    print("x1 = ", x1)
    print("x2 = ", x2)
elif d < 0:
    print("нет корней")




