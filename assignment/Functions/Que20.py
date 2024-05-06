''' Write a Python program that invokes a function after a specified period of time.
Sample Output: '''
import time
def delay():
    print("hello")

x = int(input("Enter a number :"))
time.sleep(x)
delay()