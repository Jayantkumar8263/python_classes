'''Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 83)]
'''
subject = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 83)]
subject.sort(key=lambda x: x[2])
print(subject) 
