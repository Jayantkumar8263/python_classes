''' Write a Python function to check whether a number falls within a given range. '''
def abc(a):
    if a  in range(1, 11):
        print("Number is in range")
    else:
        print("Number is not in range")
        
x = int(input("Enter a number :"))
abc(x)      