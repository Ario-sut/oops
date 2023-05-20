class student:

    def __init__(self,name, age):
        self.name = name
        self.age = age

    def printHi(self):
        print('Hi, My name is', self.name, 'I am', self.age, 'years old')

student1 = student('Halip', 23)
student2 = student('Fitraka', 19)

student1.printHi()
student2.printHi()
