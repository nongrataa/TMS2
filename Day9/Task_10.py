"""Создать родительский класс Pet, содержащий все общие методы классов Dog, Cat, Parrot.
Унаследовать Dog, Cat, Parrot от класса Pet. Удалить в дочерних классах те методы, которые имеются у родительского класса.
Создать объект каждого класса и вызвать все его методы."""

class Pet:
    def run(self):
        pass

    def jump(self):
        pass

    def birthday(self):
        self.age +=1

    def sleep(self):
        pass

class Dog(Pet):
    def __init__(self,name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def bark(self):
        pass

class Cat(Pet):
    def __init__(self,name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def meow(self):
        pass

class Parrot(Pet):
    def __init__(self,name, age, master):
        self.name = name
        self.age = age
        self.master = master

    def fly(self):
        pass



dog = Dog('Тузик',2,'Petya')
cat = Cat('Гузик',1,'Sasha')
parrot = Parrot('Бутусик',2,'Polina')

print(f'Имя - {dog.name}, возраст - {dog.age}, хозяин - {dog.master}')
dog.birthday()
print(f'Имя - {dog.name}, возраст - {dog.age}, хозяин - {dog.master}')

print(f'Имя - {cat.name}, возраст - {cat.age}, хозяин - {cat.master}')
cat.birthday()
print(f'Имя - {cat.name}, возраст - {cat.age}, хозяин - {cat.master}')

print(f'Имя - {parrot.name}, возраст - {parrot.age}, хозяин - {parrot.master}')
parrot.birthday()
print(f'Имя - {parrot.name}, возраст - {parrot.age}, хозяин - {parrot.master}')
