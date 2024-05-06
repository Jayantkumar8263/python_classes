'''Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument. '''
def abc(a):
    c = 1
    for i in range(1, a+1):
        #print(i)
        c*= i
    print(c)
    
x = int(input("Enter a number :"))
abc(x)