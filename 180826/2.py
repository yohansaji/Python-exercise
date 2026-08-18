'''
import random

for i in range(100):
    print(i,random.randint(1,10))
'''

'''
from math import sqrt, ceil, floor

print(sqrt(25))
print(ceil(4.2))
print(floor(4.8))
'''

'''
import math as m
print(m.sqrt(25))

import datetime as dt
print(dt.datetime.now())
'''

# math Module example
'''
import math

print(math.sqrt(25))
print(math.pow(2,3))
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.pi)
'''

# random Module
'''
import random

number=random.randint(1,10)
print(number)

colors=["Red","Blue","Green"]
print(random.choice(colors))
'''

# datetime Module
'''
import datetime

now=datetime.datetime.now()
print(now)

today=datetime.date.today()
print(today)
'''

# statistics Module
'''
import statistics

marks=[80,90,70,85,95]

print(statistics.mean(marks))
print(statistics.median(marks))
print(statistics.mode(marks))
'''

# os Module
'''
import os

print(os.getcwd())
print(os.listdir())

if os.path.exists("data.csv"):
    print("File exists")
else:
    print("File Doesnt Exist")
'''

# __name __ and __main__
'''
def greet():
    print("Hello")

if __name__ == "__main__":
    greet()
'''