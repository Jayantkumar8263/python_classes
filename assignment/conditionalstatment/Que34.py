''' Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.'''
x = int(input("enter a integer :"))
y = int(input("enter a integer :"))
c = x + y
if c >= 15 and c <= 20:
    print("20")
else:
    print(c)
    