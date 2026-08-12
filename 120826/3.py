#Calculator program using functions
def add(a,b):
    return a+b

def sub(a,b):
    return a-b  

def mul(a,b):
    return a*b

def div(a,b):
    return int(a/b)


x,y=map(int,input("Enter two numbers: " ).split())
print(add(x,y))
print(sub(x,y))
print(mul(x,y))
print(div(x,y))
