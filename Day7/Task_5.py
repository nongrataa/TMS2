"""Дан список имен, отфильтровать все имена, где есть буква k"""


def sortir(m):
    s = []
    for i in m:
        if 'K' in i or 'k' in i:
            s.append(i)
    return s


name_list = ['Sasha', 'Katya', 'Petya', 'Kseniya', 'Masha', 'Kostya']

print(sortir(name_list))
#
# g = map(lambda x: 'K' in x, name_list)
# print(list(g))
