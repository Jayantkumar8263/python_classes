''' 10. Write a Python program to sum all the items in a dictionary. '''
d = {
    1: 10,
    2: 20,
    3: 30
}
a = 0
b = 0
for i in d:
    a+= i
    b+= d[i]
print(a, ':', b)