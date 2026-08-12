#ATM Simulator
b=10000
c=int(input("Enter the amount to withdraw: "))
if c==0:
    print("Invalid Entry : 0")
elif c<=b:
    b-=c
    print("Withdrawal successful. Remaining balance:", b)
else:
    print("Insufficient balance. Current balance:", b)