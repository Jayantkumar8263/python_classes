'''Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird'''

n = int(input("enter a number :"))
if n % 2 != 0:
    print("weird")
if n % 2 == 0:
    for n in range(2, 5):
        print("Not Weird")
if n % 2 == 0:
    for n in range(6, 20):
        print("Weird")
elif n > 20 and n % 2 == 0:
    print("not weird")
else :
    print("Weird")