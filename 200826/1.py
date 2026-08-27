#class Demo
'''
class Student:
    def __init__(self, name, age):
        self. name = name
        self. age = age

student1= Student( "Yohan", 22)
student2= Student("Rahul", 23)
student3= Student("Anu", 21)

print(student1. name)
print(student2.name)
print(student3.name)
'''

#adding methods to class
'''
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)

student=Student("Yohan")
student.introduce()
'''

#Methods can have parameters
'''
class Student:
    def __init__(self, name):
        self.name=name

    def greet(self, person):
        print(self.name, "says hello to", person)

student=Student("Yohan")
student.greet("Rahul")
'''

#Practical Student Class
class Student:
    def __init__(self, name, age, marks):
        self.name=name
        self.age=age
        self.marks=marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)

student=Student("Yohan",22,85)
student.display()