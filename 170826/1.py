'''
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Yohan")
'''

'''
def introduce(name, age):
    print(name, age)

introduce("Yohan", 22)

introduce(age=22, name="Yohan")
'''

def calculate_total(numbers):
    total = 0

    for number in numbers:
        total += number
    return total

numbers=[10,20,30,40]
print(calculate_total(numbers))