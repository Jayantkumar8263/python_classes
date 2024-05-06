''' Write a Python program to create an instance of a specified class and display the namespace of the said instance '''
class name_space():
    def __init__(self, name, mobile, age):
        self.name = name
        self.mobile = mobile
        self.age = age
        
obj = name_space("jayant", 990719693, 19)

print(obj.name, obj.mobile, obj.age)