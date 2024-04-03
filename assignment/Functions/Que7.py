''' Write a Python function that accepts a string and counts the number of upper and lower case letters. '''
def abc(a):
    u = 0
    l = 0
    for i in a :
        if i.isupper():
            u += 1
        if i.islower():
            l += 1
    print("uppercase:", u)
    print(" lower case :", l)

x = input("Enter a string :")
abc(x)
