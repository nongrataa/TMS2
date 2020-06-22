"""Добавить новый приватный атрибут адрес(по-умолчанию равен ‘Minsk’). Добавить getter и setter для адреса."""


class City():
    def __init__(self, name, age, adress='Minsk'):
        self.name = name
        self.age = age
        self.__adress = adress

    def get_adress(self):
        return self.__adress

    def set_adress(self, adress):
        self.__adress = adress


a = City('Sacha', 25)
print(a.name, a.age, a.get_adress())
a.set_adress('Grodno')
print(a.name, a.age, a.get_adress())
