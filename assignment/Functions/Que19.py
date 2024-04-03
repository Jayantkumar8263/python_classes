'''  Write a Python program to access a function inside a function. '''
def function1():
    def function2():
        print("hello")


    function2()
    
function1()    