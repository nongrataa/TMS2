"""Дан список имен, отфильтровать все имена, где есть буква k"""

#
# def sortir(m):
#     s = []
#     for i in m:
#         if 'K' in i or 'k' in i:
#             s.append(i)
#     return s


name_list = ['Sashka', 'Katya', 'Petya', 'Kseniya', 'Masha', 'Kostya']

# print(sortir(name_list))

g = filter(lambda x: 'K' in x or 'k' in x, name_list)
print(list(g))
