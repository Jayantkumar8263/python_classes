''' Write a  Python function student_data () that will print the ID of a student (student_id). If the user passes an argument student_name or student_class the function will print the student name and class. '''

class student_data():
    def __init__(self, id, name, standard):
        self.id= id
        self.name = name
        self.standard = standard
        
obj = student_data(1234, 'abcd', 10)
print(obj.id, obj.name, obj.standard)