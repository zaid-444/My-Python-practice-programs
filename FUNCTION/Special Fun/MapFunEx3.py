# Write a python program which will accept list of old salary elements and obtain the new salary by giving 20% increament 

print("Enter list of old salaries")

oldsal = [ float(sal) for sal in input().split() ]

newsal = list(map(lambda sal: sal+sal*(20/100),oldsal))

print("-"*50)
print("Old Salary\t\tNew Salary")
print("-"*50)
for olsl,nwsl in zip(oldsal,newsal):
    print("{}\t\t\t{}".format(olsl,nwsl))

print("-"*50)