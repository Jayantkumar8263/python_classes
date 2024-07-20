'''Write a Python program to create a dictionary from two lists without losing duplicate values.
'''

a = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']

b = [1, 2, 2, 3]

c = {a[i]: b[i] for i in range(len(a))}
print(c)


"by using list_comprihention" 