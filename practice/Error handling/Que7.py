'''Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input '''
try: 
    x = int(input("enter a number"))
except:
    raise KeyboardInterrupt