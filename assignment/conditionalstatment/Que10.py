'''Write a Python program that iterates the integers from 1 to 50. For multiples of zthree print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".
Sample Output : 
fizzbuzz
1
2
fizz
4
buzz
'''

x = int(input("enter a number :"))
if x%3 == 0 and x%5 ==0:
    print("Fizzbuzz")
elif x%5 == 0:
    print("Buzz")
elif x%3 == 0:
    print("Fizz")
else:
    print("marja")
    
        