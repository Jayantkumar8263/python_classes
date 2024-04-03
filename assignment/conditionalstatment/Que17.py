'''
Write a Python program to print the alphabet pattern 'A'.
Expected Output:

  ***                                                                   
 *   *                                                                  
 *   *                                                                  
 *****                                                                  
 *   *                                                                  
 *   *
 *   * 
 '''
for i in range(7):
    for j in range(5):
        if i == 0 and j in (1, 2, 3):
            print("*",end="")
        elif i == 1 and j in (0, 4):
            print("*",end="")
        elif i == 2 and j in (0,4):
            print("*",end="")
        elif i == 3 and j in (0, 1, 2, 3, 4):
            print("*",end="")
        elif i == 4 and j in (0, 4):
            print("*",end="")
        elif i == 5 and j in (0, 4):
            print("*",end="")
        elif i == 6 and j in (0, 4):
            print("*",end="")    
        else:
            print(" ",end="")
    print()
            
        