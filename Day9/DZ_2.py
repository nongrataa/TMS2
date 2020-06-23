"""Создать класс Car. Атрибуты: марка, модель, год  выпуска, скорость(по умолчанию 0).
Методы: увеличить скорости(скорость + 5), уменьшение скорости(скорость  - 5),
стоп(сброс скорости на 0), отображение скорости, разворот(изменение знака скорости). Все атрибуты приватные."""


class Car:
    def __init__(self, brand, model, ear, speed=0):
        self.brand = brand
        self.model = model
        self.ear = ear
        self.speed = speed

    def add_speed(self):
        self.speed += 5

    def dec_speed(self):
        self.speed -= 5

    def stop_speed(self):
        self.speed = 0

    def show_speed(self):
        return self.speed

    def turn_back(self):
        self.speed *= -1


car = Car('Mersedes','AMG',2018,100)
print(car.show_speed())
car.add_speed()
print(car.show_speed())
