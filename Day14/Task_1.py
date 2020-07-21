from scipy.integrate import quad


def integrand(x, a, b):
    return a*x**2+b


a = 2
b = 1
i = quad(integrand, 0, 1, args=(a, b))

print(i)