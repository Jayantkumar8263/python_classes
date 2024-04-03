'''
 Write a Python program to check if a triangle is equilateral, isosceles or scalene.
Note :
An equilateral triangle is a triangle in which all three sides are equal.
A scalene triangle is a triangle that has three unequal sides.
An isosceles triangle is a triangle with (at least) two equal sides.
Expected Output:

Input lengths of the triangle sides:                                    
x: 6                                                                    
y: 8                                                                    
z: 12                                                                   
Scalene triangle  
'''
x = int(input("enter a number :"))
y = int(input("enter a number :"))
z = int(input("enter a number :"))
if x == y and x == z and y == z :
    print("equilateral triangle")
if x != y and y!= z and z != x :
    print("scalene triangle") 
if x == y or y != z :
    print("isosceles triangle")
else:
    print("it is not a triangle")
    
    