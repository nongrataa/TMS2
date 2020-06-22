"""Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age. Класс имеет три метода: jump, run, bark.
Каждый метод выводит сообщение на экран. Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты."""


class dog():
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print('Jump')

    def run(self):
        print('Run')

    def bark(self):
        print("Bark")


a = dog(21, 12, 'Гузик', 3)

a.run()
a.jump()
a.bark()
print(a.name, a.height, a.age, a.weight)
