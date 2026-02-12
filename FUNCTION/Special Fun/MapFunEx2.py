# Write a python program which will accept list of old salary elements and obtain the new salary by giving 20% increament 

print("Enter list of old salaries")

incrsal = lambda sal: sal+sal*(20/100)

oldsal = [ int(sal) for sal in input().split() ]

nwsal = list(map(incrsal,oldsal))

print("-"*50)
print("Old Salary\t\tNew Salary")
print("-"*50)
for oldsl,newsl in zip(oldsal,nwsal):
    print("{}\t\t\t{}".format(oldsl,newsl))
print("-"*50)