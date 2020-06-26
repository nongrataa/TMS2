"""Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age. Класс имеет три метода: jump, run, bark.
Каждый метод выводит сообщение на экран. Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты."""


"""Читаем из файла список имен животных и тд, добавляем в дикт потом ищем по имени и если есть выводим все данные о нем"""

class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self.my_list = [

        ]

    def jump(self):
        print('Jump')

    def run(self):
        print('Run')

    def bark(self):
        print("Bark")

    def open_file(self):
        with open('ffile.txt') as my_file:
            f = my_file.readlines()
            for i in f:
                self.my_list.append(
                    {
                        "name": i.split(',')[0],
                        "age": i.split(',')[1],
                        "weight": i.split(',')[2],
                        "height": i.split(',')[3]
                    }
                )
        return self.my_list

    def find_animal(self, name):
        for i in self.my_list:
            if name == i.get('name'):
                print(i)



a = Dog(21, 12, 'Гузик', 3)

a.open_file()
a.find_animal('Bob')
# a.run()
# a.jump()
# a.bark()
# print(a.name, a.height, a.age, a.weight)
