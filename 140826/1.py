m=[]
t=0
n=int(input("Enter the number of subjects:"))
for i in range(1,n+1):
    m.append(int(input(f"Enter the marks for subject {i}: ")))
    t+=m[i-1]

print(m)
print(f"Total marks: {t}")
print("Average = ",t/n)