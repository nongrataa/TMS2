""" Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и меняет атрибут имени у объекта.
Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя."""

class dog():
    def __init__(self, name):
        self.name = name
    def change_name(self, name_change):
        self.name = name_change


a = dog('Бобик')
print(a.name)
a.change_name('Гузик')
print(a.name)