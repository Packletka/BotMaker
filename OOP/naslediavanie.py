class Person:
    def can_walk(self):
        print('Я могу дышать')


class Doctor(Person):
    def can_cure(self):
        print('Я могу лечить')


class Architect(Person):
    def can_built(self):
        print('Я могу строть')


d = Doctor()
a = Architect()
print(issubclass(Doctor, Person))
print(issubclass(Person, Doctor))
print(isinstance(d, Doctor))
print(isinstance(d, Person))
