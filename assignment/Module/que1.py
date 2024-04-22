''' Write a Python program to generate a random color hex, a random alphabetical string, random value between two integers (inclusive) and a random multiple of 7 between 0 and 70. Use random.randint() '''

import random
import string
def bcd (d):
    return u'#{random.randint(0, 0xFFFFFF):06x}'
def abc (s):
    return random.randint(0, 10)*7
print(random.randint(0, 10)*7)
print(u'#{random.randint(0, 0xFFFFFF):06x}')