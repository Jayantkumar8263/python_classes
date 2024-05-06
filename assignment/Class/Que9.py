''' Write a  Python class named Student with two attributes student_name, marks. "Modify the attribute values of the said class" and print the original and modified values of the said attributes '''

class student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
obj = student("zyxw", 78)
print(obj.name)
#print(obj.marks)