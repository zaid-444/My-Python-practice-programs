# Write a python program which will accept list of old salary elements and obtain the new salary by giving 20% increament 

def incrment(sal):
    sal = sal+sal*(20/100)
    return int(sal)

print("Enter List of Old Salaries")
oldsal = [ int(sal) for sal in input().split() ]


print("="*60)
nsl = list(map(incrment,oldsal))
print("Old Salary\t\tNew Salary")
print("="*60)
for old,newsl in zip(oldsal,nsl):
    print("{}\t\t\t{}".format(old,newsl))
print("="*60)