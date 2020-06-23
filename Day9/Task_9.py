"""Создать три класса: Dog, Cat, Parrot. Атрибуты каждого класса: name, age, master.
Каждый класс содержит конструктор и методы: run, jump, birthday(увеличивает age на 1), sleep.
Класс Parrot имеет дополнительный метод fly. Cat - meow, Dog - bark."""


class Dog:
    def __init__(self, name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def run(self):
        pass

    def jump(self):
        pass

    def birthday(self):
        self.age += 1

    def sleep(self):
        pass

    def bark(self):
        pass

#
# class Cat:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self):
#         pass
#
#     def jump(self):
#         pass
#
#     def birthday(self):
#         self.age += 1
#
#     def sleep(self):
#         pass
#
#     def meow(self):
#         pass
#
#
# class Parrot:
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self):
#         pass
#
#     def jump(self):
#         pass
#
#     def birthday(self):
#         self.age += 1
#
#     def sleep(self):
#         pass
#
#     def fly(self):
#         pass


dog = Dog('Тузик', 2, 'Petya')
# cat = Cat('Гузик', 1, 'Sasha')
# parrot = Parrot('Бутусик', 2, 'Polina')

print(f'Имя - {dog.name}, возраст - {dog.age}, хозяин - {dog.master}')
dog.birthday()
print(f'Имя - {dog.name}, возраст - {dog.age}, хозяин - {dog.master}')
#
# print(f'Имя - {cat.name}, возраст - {cat.age}, хозяин - {cat.master}')
# cat.birthday()
# print(f'Имя - {cat.name}, возраст - {cat.age}, хозяин - {cat.master}')
#
# print(f'Имя - {parrot.name}, возраст - {parrot.age}, хозяин - {parrot.master}')
# parrot.birthday()
# print(f'Имя - {parrot.name}, возраст - {parrot.age}, хозяин - {parrot.master}')
