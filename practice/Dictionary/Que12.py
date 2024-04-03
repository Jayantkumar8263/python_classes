''' 12. Write a Python program to remove a key from a dictionary '''
d = {
    'name' : 'JAY',
    'age' : 19,
    'add' : 'ruabandha sector'
    }
if 'name'in d:
    del d['age']
print(d)    