"""Создать декоратор для функции, которая принимает список чисел.
Декоратор должен производить предварительную проверку данных - удалять все четные элементы из списка."""


# def decorate(func):
#     def results(datas):
#         result = []
#         for i in datas:
#             if i % 2 != 0:
#                 result.append(i)
#         func(result)
#
#     return results
#
#
# @decorate
# def result(datas):
#     print(datas)
#
#
# result([1, 2, 3, 4, 5])


"""Передаем список ['a', 'b', 'c', 'd'] нужно вернуть дикт вида {1: 'a', 2: 'b', 3: 'c', 4: 'd'} """
def decorate(func):
    def results(datas):
        my_dict = {}
        my_dict = enumerate(datas, 1)
        func(my_dict)

    return results


@decorate
def result(datas):
    print(dict(datas))


result(['a', 'b', 'c', 'd'])
