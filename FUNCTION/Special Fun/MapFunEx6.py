print("Enter List of Salaries separated by space")
sallist = [ int(val) for val in input().split() ]
print("Enter List of Commition separated by space")
comlist = [ int(val) for val in input().split() ]

if len(sallist) > len(comlist):
    for i in range(len(sallist) - len(comlist)):
        comlist.append(0)

if len(comlist) > len(sallist):
    for i in range(len(comlist)-len(sallist)):
        sallist.append(0)

total = list(map(lambda sal,com: sal+com,sallist,comlist))
print("-"*50)
print("Salary\t\tCommition\tTotal")
print("-"*50)

for sal,com,to in zip(sallist,comlist,total):
    print("{}\t\t{}\t\t{}".format(sal,com,to))
print("-"*50)