'''Write a Python function that prints out the first n rows of Pascal's triangle.
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
'''
def pascal_triangle(e):
    for i in range(e):
        a = 1
        for j in range(0,  i + 1): 
            print(a, end=" ")
            a = a*(i-j)//(j+1)
        print()
a = int(input("enter a number :"))
pascal_triangle(a)