#22. Challenge ⭐ — Student Analyzer
#Build a reusable function that accepts a student dictionary.


def analyze_student(student):
    total=0

    name=student[0]
    student.pop(0)

    highest=student[0]
    lowest=student[0]

    for i in student:
        total+=i

        if i>highest:
            highest=i

        if i<lowest:
            lowest=i

    avg=total/len(student)
    return{
        "name": name,
        "total": total,
        "average": avg,
        "highest": highest,
        "lowest": lowest
    }
    
    



l=[]
n=input("Enter the name of the student: ")
l.append(n)
s=int(input("Enter the number of subjects: "))
for i in range(1,s+1):
    u=int(input(f"Enter Mark {i} "))
    l.append(u)
print(l)

print(analyze_student(l))
