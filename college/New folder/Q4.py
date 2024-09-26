'''conversion of temp'''

temp = int(input("Enter the temprature :"))
unit = int(input("Enter the unit :"))

if unit == 1:
    c = ((temp-32)/9)*5
    print(c)
if unit == 2:
    f = ((9/5)*temp)+32
    print(f)