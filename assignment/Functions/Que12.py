'''Write a Python function that checks whether a passed string is a palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
'''
def pelindrome(d):
    if d == d[::-1]:
        print(True)
    else:
        print(False)

x = input("enter a word :")
pelindrome(x)