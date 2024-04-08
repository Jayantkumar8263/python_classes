''' Write a Python program to replace the last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)] '''

a = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
for i in a :
    print(i[:-1] + (100,))