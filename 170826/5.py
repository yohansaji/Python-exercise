#Task 4- Maximum
'''
def find_max(a,b):
    if a>b:
        return a
    else:
        return b

print(find_max(1,2))
print(find_max(2,1))
'''

#Task 5- Average
'''
def calculate_average(numbers):
    total=0
    for i in numbers:
        total+=i
    return total/len(numbers)

x=(1,2,3,4,5)
print(calculate_average(x))

#Task 6- Result
'''
'''
def check_result(mark):
    if mark>90:
        return "Excellent"
    elif mark>75:
        return "Very Good"
    elif mark>50:
        return "Pass"
    else:
        return "Fail"

x=(48,72,88,99)
for i in x:
    print(check_result(i))

'''