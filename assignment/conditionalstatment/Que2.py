''' Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
 Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
 Expected Output :
 45°F is 7 in Celsius'''

temp = int(input("enter a temperature :"))
unit = int(input("1 for c-f and 2 for f-c"))
if unit == 1:
    f = ((9/5)*temp)+32
    print(f)
elif unit == 2:
    c = ((temp-32)/9)*5
    print(c)