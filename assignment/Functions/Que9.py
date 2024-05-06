''' Write a Python function that takes a number as a parameter and checks whether the number is prime or not. '''
def abc():
    x = int(input("Enter a number :"))
    if x == 1 or x == 2:
        print("it is a prime number")
    else:
        for i in range(2, x):
            if x % i == 0:
                print("it is not a prime number")
                break
        print("it is a prime number")
abc()