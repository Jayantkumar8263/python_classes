''' Write a  Python class named Student with two attributes student_id, student_name. Add a new attribute student_class and display the entire attribute and the values of the class. Now remove the student_name attribute and display the entire attribute with values '''

class student():
    def __init__(self, id):
        self.id = id
        #self.name = name
class student_class():
    def __init__(self, standard):
        self.standard = standard
          
obj1 = student(1234)
obj2 = student_class(12)

print(obj1.id, )
print(obj2.standard)