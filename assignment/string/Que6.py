'''Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.'''
x = input("Enter a string :")
y = "ing"
print(x + y)
'''if x [-3:] == 'ing' :
    print(x[:-3] += 'ly')
else:
    print(x)'''