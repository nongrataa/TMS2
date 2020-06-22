"""Сделать все атрибуты класса Dog приватными. Сделать для каждого атрибута getter и setter используя декораторы.
Все change методы удалить"""

class Dog():
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height

    @property
    def get_name(self):
        return self.__name

    @property
    def get_age(self):
        return self.__age

    @property
    def get_height(self):
        return self.__height

    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age

    @height.setter
    def height(self, height):
        self.__height = height
