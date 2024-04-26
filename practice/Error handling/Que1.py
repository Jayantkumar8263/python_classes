''' Write a  Python program to handle a ZeroDivisionError exception when dividing a number by zero.'''


try:
    x = int(input("enter a number :"))
    y = int(input("enter a number :"))
    c = (x/y)
    print(c)
except ZeroDivisionError :
    print("error")