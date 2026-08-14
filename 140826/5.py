m=[85,72,91,64,78,88,55]
t=0
for i in m:
    t+=i
print("Total marks: ",t)
print("Average marks: ",t/len(m))
m.sort()
print("Highest marks: ",m[-1])
print("Lowest marks: ",m[0])
print("Number of students: ",len(m))

