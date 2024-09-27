class Person(object):
    pass


class Docktor(Person):
    pass


class Architect(Person):
    pass


print(issubclass(Person, object))
print(dir(object))
a = Person()
print(a.__hash__())
