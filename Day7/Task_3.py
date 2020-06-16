"""Создать lambda функцию, которая принимает на вход список имен и выводит их в формате “Hello, {name}” в другой список"""
my_list = ['Sasha', 'Masha', 'Dasha', 'Dima', 'Petya']

my_list2 = [2, 4, 4, 6, 7]

g = map(lambda x: f'Hello {x}', my_list)

print(list(g))
