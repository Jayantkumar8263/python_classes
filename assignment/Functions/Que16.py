''' Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).
'''
def square(a):
    x = 1
    for s in range(1, 31):
        if s <= 30 :
            print(s*s)
        else:
            print('invalid')
s = int(input("enter a number :"))
square(s)