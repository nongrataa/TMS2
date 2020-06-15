"""Создать универсальный декоратор, который меняет порядок аргументов в функции на противоположный. """


# def decorate(func):
#     def results(*args):
#         args = args[::-1]
#         func(*args)
#     return results
#
#
# @decorate
# def result( *args):
#     print(args)
#
# result(1,2,3,4,5)


def decorate(func):
    def results(*args, **kwargs):
        # data = {}
        # for i, j in kwargs.items():
        #     data[str(j)] = str(i)
        # func(**data)
        data = {}
        for i, j in kwargs.items():
            if j in args:
                continue
            data[i] = j
        func(**data)

    return results


@decorate
def result(*args, **kwargs):
    print(args, kwargs)


result(1, 2, 3, 4, 9, a='1', b='2', c='3', d='4', e='5')
