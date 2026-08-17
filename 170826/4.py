#Task 1- Greeting
'''
def greet(name):
    print("Hello ",name)
    print("Welcome to the club")


name=("Milan","Thomson","Yohan")
for n in name:
    greet(n)
'''

#Task 2- Add
'''
def add(a,b):
    return a+b

print(add(10,20))
print(add(50,25))
'''

#Task 3- Even/Odd
'''
def check_even_odd(number):
    if number==0:
        return "Zero"
    elif number%2==0:
        return "Even"
    else:
        return "Odd"

a=(0,1,2,3,4,5,6,7,8,9,0)
for i in a:
    print(i,check_even_odd(i))
'''