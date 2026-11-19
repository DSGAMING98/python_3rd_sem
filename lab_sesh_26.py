class Student:
    def __init__(self, name):
        self.name = name

    def hi(self):
        print(self.name)


s1 = Student("Prajwal")
s1.hi()