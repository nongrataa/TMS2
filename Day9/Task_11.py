"""Добавить два новых атрибута в родительский класс: weight и height.
Добавить методы change_weight, change_height принимающий один параметр и прибавляющий его к соответствующему аргументу.
В случае если параметр не был передан, увеличивать на 0.2.
Изменить метод fly класса Parrot. Если вес больше 0.1 выводить сообщение This parrot cannot fly.
"""


class Pet:
    def __init__(self, name, age, master, weight, height):
        self.weight = weight
        self.height = height
        self.name = name
        self.age = age
        self.master = master

    def change_weight(self, weight=0.2):
        self.weight += weight

    def change_height(self, height=0.2):
        self.height += height

    def run(self):
        pass

    def jump(self):
        pass

    def birthday(self):
        self.age += 1

    def sleep(self):
        pass


class Dog(Pet):

    def bark(self):
        pass


class Cat(Pet):

    def meow(self):
        pass


class Parrot(Pet):

    def fly(self):
        if self.weight > 0.1:
            print('This parrot cannot fly')


dog = Dog('Тузик', 2, 'Petya', 50, 30)
cat = Cat('Гузик', 1, 'Sasha', 10, 10)
parrot = Parrot('Бутусик', 2, 'Polina', 0.2, 5)

print(f'Имя - {dog.name}, возраст - {dog.age}, хозяин - {dog.master}')
dog.birthday()
print(f'Имя - {dog.name}, возраст - {dog.age}, хозяин - {dog.master}')

print(f'Имя - {cat.name}, возраст - {cat.age}, хозяин - {cat.master}')
cat.birthday()
print(f'Имя - {cat.name}, возраст - {cat.age}, хозяин - {cat.master}')

print(f'Имя - {parrot.name}, возраст - {parrot.age}, хозяин - {parrot.master}, рост - {parrot.height}')
parrot.birthday()
print(f'Имя - {parrot.name}, возраст - {parrot.age}, хозяин - {parrot.master}, рост - {parrot.height}')

parrot.fly()
