''' Write a Python program to create two empty classes, Student and Marks. Now create some instances and check whether they are instances of the said classes or not. Also, check whether the said classes are subclasses of the built-in object class or not '''

class empty_class():
    def __init__(self, student, standard):
        self.student = student
        self.standard = standard
        
obj = empty_class("abc", 10)

print(obj.student)
print(obj.standard)