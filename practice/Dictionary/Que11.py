'''11. Write a Python program to multiply all the items in a dictionary.
'''
d = {
    1: 2,
    3: 4, 
    5: 6,
}
a = 1
b = 1
for i in d :
    a*= i
    b*= d[i]
print(a, ':', b)
    