class Mark:
    def __init__(self, values):
        self.value = values
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        print('call next Marks')
        if self.index >= len(self.value):
            raise StopIteration
        letter = self.value[self.index]
        self.index += 1
        return letter


class Student:
    def __init__(self, name, surname, marks):
        self.marks = marks
        self.name = name
        self.surname = surname

    def __getitem__(self, item):
        return self.name[item]

    def __iter__(self):
        print("Call iter")
        self.index = 0
        return iter(self.marks)

    def __next__(self):
        print('call next Student')
        if self.index >= len(self.surname):
            raise StopIteration
        letter = self.surname[self.index]
        self.index += 1
        return letter

m = Mark([3, 4, 5, 6, 7])
igor = Student('Igor', 'Nikolaev', m)
for i in igor:
    print(i)
