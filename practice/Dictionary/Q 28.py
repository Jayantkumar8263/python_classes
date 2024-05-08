'''Write a Python program to sort a list alphabetically in a dictionary'''
d = {'red' : 1,'blue' : 2,'green' :3}
d1 = list(d)
print(d1)
for i in sorted(d1):
    print(d1[i])