"""Переопредилить метод таким образом что когда мы воодим город нам выводило страну в которой он находится"""


class A:
    def __init__(self):
        self.country = {
            'Minsk': 'Belarus',
            'Moscow': 'Russia',
            'Kiev': 'Ukrain'
        }

    @property
    def get_country(self):
        self.country


class B(A):
    def get_country(self, city):
        return self.country[city]


b = B()
print(b.get_country('Minsk'))
