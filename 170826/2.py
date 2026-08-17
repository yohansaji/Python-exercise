#Functions + Dictionaries
'''
def display_student(student):
    print("Name:", student["name"])
    print("Marks:", student["marks"])

student = {"name": "Yohan", "marks": 85}
display_student(student)
'''
'''
#Functions + Conditions
def check_result(marks):
    if marks >= 50:
        return "Pass"
    else:
        return "Fail"
print(check_result(75))
print(check_result(35))
'''
'''
#Functions + Loops
def print_numbers(numbers):
    for number in numbers:
        print(number)

numbers = [10,20,30]
print_numbers(numbers)
'''
'''
#Local Variables
def calculate():
    result=100
    print(result)

calculate()
print(result) # This will raise an error since 'result' is a local variable and not accessible outside the function.
'''
'''
#Global Variables
name="Yohan"
def greet():
    print(name)

greet()
'''