'''Write a Python function that prints out the first n rows of Pascal's triangle.
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
'''
def pascal_triangle():
    
    for i in range(10):
        a = 1
        for j in range(0,  i + 1): 
            print(a, end=" ")
            a = a*(i-j)//(j+1)
        print()
pascal_triangle()