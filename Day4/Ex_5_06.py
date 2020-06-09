"""
Создать список учеников подобной структуры. Определить средний балл оценок по всем предметам,
и вывести сведения о студентах, средний балл которых больше 4
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
        'informatics': 10,
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

def inf_student(list):
    for i in puplist:
        sum = 0
        average = 0
        for key, value in i.items():
            if key == 'phyisics' or key == 'informatics' or key == 'history':
                sum = sum + int(value)
        average = sum / 3
        if average > 7:
                print(f"Имя студента - {i['Firstname']} \nГруппа - {i['Group']} \nОценки по предметам: \nФизика - {i['phyisics']} \nИнформатика - {i['informatics']} \nИстория - {i['history']}")
                print(f'Средний бал студента - {average} \n')

    return

inf_student(puplist)