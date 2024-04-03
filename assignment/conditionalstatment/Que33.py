''' Write a Python program to convert a month name to a number of days.
Expected Output:

List of months: January, February, March, April, May, June, July, August
, September, October, November, December                                
Input the name of Month: February                                       
No. of days: 28/29 days 
'''

x = input("enter the month :")
if x == ("january"):
    print("Number of days = 31")
elif x == ("febuary"):
    print("Number of days = 28/29")
elif x == ("march"):
    print("Number of days = 31")
elif x == ("april"):
    print("Number of days = 30")
elif x == ("May"):
    print("Number of days = 31")
elif x == ("june") :
    print("Number of days = 30")
elif x == ("julay"):
    print("Number of days = 31")
elif x == ("august"):
    print("Number of days = 30")
elif x == ("septemer"):
    print("Number of days = 31")
elif x == ("octuber"):
    print("Number of days = 30")
elif x == ("november"):
    print("Number of days = 31")
elif x == ("december"):
    print("Number of days = 30")
else:
    print("invalid")