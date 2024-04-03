''' Write a Python program to display the sign of the Chinese Zodiac for the given year in which you were born.
Expected Output:

Input your birth year: 1973                                             
Your Zodiac sign : Ox
'''
 
x = int(input("enter the year :"))
if x%12 == 0:
    print("monkey")
elif x%12 == 1:
    print("Rooster")
elif x%12 == 2:
    print("Dog")
elif x%12 == 3:
    print("Pig")
elif x%12 == 4:
    print("Rat")
elif x%12 == 5:
    print("Ox")
elif x%12 == 6:
    print("Tiger")
elif x%12 == 7:
    print("Rabbit")
elif x%12 == 8:
    print("Dragon")
elif x%12 == 9:
    print("Snake")
elif x%12 == 10:
    print("Horse")
elif x%12 == 11:
    print("Sheep")