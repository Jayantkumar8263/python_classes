'''Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer. '''
try: 
    x = int(input("enter a number :"))
except:
    raise ValueError