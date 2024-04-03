'''Write a Python program to display the astrological sign for a given date of birth.
Expected Output:

Input birthday: 15                                                      
Input month of birth (e.g. march, july etc): may                        
Your Astrological sign is : Taurus
'''
x = int(input("enter a number :"))
y = input("enter a month :")
if x <=19 and y == "january":
    print("Your Astrological sign is : Capricorn")
elif x <= 18 and y == "febuary" :
     print("Your Astrological sign is : Aquarrius")
elif x <= 20 and y == "march":
     print("Your Astrological sign is : Pisces")
elif x <= 19 and y == "april":
     print("Your Astrological sign is :Taurus")
elif x <= 20 and y == "may":
     print("Your Astrological sign is : Gemini")
elif x <= 20 and y == "june":
     print("Your Astrological sign is : Cancer ")
elif x <= 20 and y == "july":
     print("Your Astrological sign is : Leo")
elif x <= 20 and y == "august":
     print("Your Astrological sign is : Virgo")
elif x <= 20 and y == "september":
     print("Your Astrological sign is : Libra")
elif x <= 20 and y == "october":
     print("Your Astrological sign is : Scorpio")
elif x <= 20 and y == "november":
    print("Your Astrological sign is : Scorpio")
elif x <= 20 and y == "december":
    print("Your Astrological sign is : Sagittarius")    
else:
    print("invalid")
    

    