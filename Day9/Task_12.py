class Person:
    def __init__(self, name, midlname, age):
        self.name = name
        self.midlname = midlname
        self.age = age
        self.predmet = []
        self.mark = []
        self.person = []


class Student(Person):

    def all_teacher(self):
        print(self.person)

    @property
    def get_teacher(self):
        return self.person

    @get_teacher.setter
    def get_teacher(self, person):
        self.person.append(person.name)
        self.person.append(person.midlname)
        self.person.append(person.age)
        self.person.append(person.predmet)
        self.person.append(person.mark)


class Teacher(Person):

    def all_student(self):
        print(self.person)

    @property
    def student(self):
        return self.person

    @student.setter
    def student(self, person):
        self.person.append(person.name)
        self.person.append(person.midlname)
        self.person.append(person.age)
        self.person.append(person.predmet)
        self.person.append(person.mark)


t = Teacher('Dmitriy', 'Vladimirovich', 35)
s = Student('Pasha', 'Dmitrievich', 25)

s.predmet = ['Математика', 'Физика', 'ЭВМ']
s.mark = ['5', '6', '4']

b = Student('Dima', 'Vasilievich', 22)
b.predmet = ['Математика', 'Физика', 'ЭВМ']
b.mark = ['4', '6', '3']

t.student = s
t.student = b


t.predmet = ['Математика', 'Физика', 'ЭВМ']
t.mark = ['4', '6', '3']
s.get_teacher = t

t.all_student()
s.all_teacher()
