def result(a, b, c, d):
    """

    :param a: number
    :type a: int
    :param b: number
    :type b: int
    :param c: string
    :type c: str
    :param d:
    :type d: bool
    :return:
    :type:int
    """
    if d is False:
        a, b = b, a

    if c == '+':
        return a + b
    elif c == '/':
        if b == 0:
            return print('деление на ноль')
        else:
            return a / b
    elif c == '*':
        return a * b
    elif c == '-':
        return a - b


print(result(5, 1, '/'), False)
