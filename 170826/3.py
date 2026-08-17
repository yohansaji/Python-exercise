#19. Practical Example — Student Analyzer
#Combine functions, lists, loops, conditions, and dictionaries.


def analyze_marks(marks):
    total=0
    highest=marks[0]
    lowest=marks[0]

    for mark in marks:
        total += mark
        if mark > highest:
            highest = mark
        if mark < lowest:
            lowest = mark

    average=total/len(marks)
    return total, average, highest, lowest


marks=[85,72,91,64,78]

total, average, highest, lowest = analyze_marks(marks)
print(total)
print(average)
print(highest)
print(lowest)