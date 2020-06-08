"""
Создать список учеников подобной структуры. Определить средний балл оценок по всем предметам, и вывести сведения о студентах, средний балл которых больше 4
pupils = [
  {
        'firstname': 'Masha',
        'Group': 42,
        'physics': 7,
        'informatics': 6,
        'history': 8,
  },
]
"""

puplist = [
    {
        'Firstname': 'Aliaksandr',
        'Group': 41,
        'phyisics': 7,
        'informatics': 6,
        'history': 9,
    },
    {
        'Firstname': 'Polina',
        'Group': 31,
        'phyisics': 5,
        'informatics': 4,
        'history': 7,
    },
    {
        'Firstname': 'Mariya',
        'Group': 32,
        'phyisics': 3,
        'informatics': 5,
        'history': 6,
    }
]

sum = 0
for i in puplist:
    print(i)
    for key, value in i.items():
        # print(f'key - {key} value - {value}')
        if key == 'phyisics':
            print(value)
            sum = sum + int(value)
        if key == 'informatics':
            print(value)
            sum = sum + int(value)
        if key == 'informatics':
            print(value)
            sum = sum + int(value)

    print(f' average - {sum/3}')

print(sum)
