''' Write a  Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error '''
try:
    x = int(input("enter a number :"))
    y = int(input("enter a number :"))
    c = x*y
    print(c)
except:
    raise ArithmeticError