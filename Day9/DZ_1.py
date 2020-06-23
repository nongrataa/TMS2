"""Создать пять классов описывающие реальные объекты.
Каждый класс должен содержать минимум три приватных атрибута, конструктор, геттеры и сеттеры для каждого атрибута,
два метода."""


class Car:
    def __init__(self, brand, speed, color):
        self.__brand = brand
        self.__speed = speed
        self.__color = color

    @property
    def brand(self):
        return self.__brand

    @property
    def speed(self):
        return self.__speed

    @property
    def color(self):
        return self.__color

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @color.setter
    def color(self, color):
        self.__color = color

    def add_speed(self, speed):
        self.__speed += speed

    def change_color(self, color):
        self.__color = color


class House:
    def __init__(self, room, color, floor):
        self.__room = room
        self.__color = color
        self.__floor = floor

    @property
    def room(self):
        return self.__room

    @property
    def color(self):
        return self.__color

    @property
    def floor(self):
        return self.__floor

    @room.setter
    def room(self, room):
        self.__room = room

    @color.setter
    def color(self, color):
        self.__color = color

    @floor.setter
    def floor(self, floor):
        self.__floor = floor


class Cat:
    def __init__(self, name, jump, master):
        self.__name = name
        self.__jump = jump
        self.__master = master

    @property
    def name(self):
        return self.__name

    @property
    def jump(self):
        return self.__jump

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    @jump.setter
    def jump(self, jump):
        self.__jump = jump

    @name.setter
    def name(self, name):
        self.__name = name

    def change_master(self, master):
        self.__master = master

    def change_jump(self, jump):
        self.__jump = jump


class Dog:
    def __init__(self, name, jump, master):
        self.__name = name
        self.__jump = jump
        self.__master = master

    @property
    def name(self):
        return self.__name

    @property
    def jump(self):
        return self.__jump

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

    @jump.setter
    def jump(self, jump):
        self.__jump = jump

    @name.setter
    def name(self, name):
        self.__name = name

    def change_master(self, master):
        self.__master = master

    def change_jump(self, jump):
        self.__jump = jump


car = Car('Mercedes', 300, 'red')
print(car.color)
car.color = 'green'
print(car.color)

dog = Dog('Тузик', 2, 'Дима')
print(f'Имя - {dog.name}, возраст - {dog.jump}, хозяин - {dog.master}')
dog.change_master('Петя')
print(f'Имя - {dog.name}, возраст - {dog.jump}, хозяин - {dog.master}')
