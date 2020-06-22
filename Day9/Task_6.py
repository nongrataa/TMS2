"""Добавить в метод инициализации новый приватный атрибут - master.
Создать метод get_master() который возвращает значение атрибута master."""


class dog():
    def __init__(self, age, name, master):
        self.age = age
        self._name = name
        self.__master = master

    def get_master(self):
        return self.__master


a = dog(10, 'Гузик', 'Бутусик')
print(a.age)
print(a._name)
print(a._dog__master)
print(a.get_master())
print(a.__master)
