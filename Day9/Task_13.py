"""
Читаем Json
показываем данные
добавлем

"""
import json


class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self.my_list = []

    def jump(self):
        print('Jump')

    def run(self):
        print('Run')

    def bark(self):
        print("Bark")

    def open_file(self):
        with open('task4.json') as my_file:
            for i in json.load(my_file):
                self.my_list.append(i)


    def add_data(self):
        my_dict = {}
        my_dict['name'] = str(input('Введите имя - '))
        my_dict['age'] = int(input('Введите возраст - '))
        my_dict['height'] = int(input('Введите рос - '))
        my_dict['weight'] = int(input('Введите вес - '))
        self.my_list.append(my_dict)
        print(self.my_list)

    def save_file(self):
        with open('task4.json', 'w') as my_file:
            json.dump(self.my_list, my_file)


a = Dog(21, 12, 'Гузик', 3)

a.open_file()
a.add_data()
a.save_file()
