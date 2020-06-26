"""Переопределить методы change_weight, change_height в классе Parrot.
В случае не передачи параметра - вес изменяется на 0.05"""


class Parrot:
    weight = 10
    def change_weight(self):
        print('Weight', self.weight)

    def change_height(self):
        print('Height')


class A(Parrot):
    def change_weight(self, weight=0.05):
        self.weight += weight
        return self.weight

parrot = Parrot()
parrot.change_weight()

a = A()
print(a.change_weight())
