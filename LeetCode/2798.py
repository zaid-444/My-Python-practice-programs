# 2798. Number of Employees Who Met the Target

def fun(hours,target):
    count = 0
    for emp in hours:
        if emp >= target:
            count += 1
    return count

hours = [ int(i) for i in input("Enter Hours: ").split() ]
target = int(input("Enter Target hour: "))

print("-"*50)
res = fun(hours,target)
print("No. of Employee met the Target =",res)
print("-"*50)
