''' Write a Python class named Student with two attributes: student_id, student_name. Add a new attribute: student_class. Create a function to display all attributes and their values in the Student class '''

class student():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
class student_class():        
    def __init__(self, standard):
        self.standard = standard
        
obj = student('name', 8569)
print(obj.name)
print(obj.id)