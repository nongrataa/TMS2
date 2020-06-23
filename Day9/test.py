class Car:
    def __init__(self, brand, speed, color):
        self.__brand = brand
        self.speed = speed
        self.__color = color

    @property
    def get_brand(self):
        return self.__brand

    @property
    def get_speed(self):
        return self.speed

    @property
    def get_color(self):
        return self.__color

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @speed.setter
    def speed(self, speed):
        self.speed = speed

    @color.setter
    def color(self, color):
        self.__color = color

    def add_speed(self, speed):
        self.__speed += speed

    def change_color(self, color):
        self.__color = color