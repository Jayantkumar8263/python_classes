'''Write a Python class named Student with two instances student1, student2 and assign values to the instances' attributes. Print all the attributes of the student1, student2 instances with their values in the given format '''


class student_class():
    def __init__(self, name, id, mobile, age):
        self.name = name
        self.id = id
        self.mobile = mobile
        self.age = age
        
obj1 = student_class('Jayant', 1200, 1234, 19)
obj2 = student_class('Jai', 1201, 5678, 19)
obj3 = student_class('P.J', 1202, 6734, 19)

print(obj1.name, obj1.id, obj1.mobile, obj1.age)
print(obj2.name, obj2.id, obj2.mobile, obj2.age)
print(obj3.name, obj3.id, obj3.mobile, obj3.age)