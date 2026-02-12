sallist = [100,200,300,400]
commlist = [10,20,30,40]
total = list(map(lambda sal,comm: sal+comm, sallist,commlist))

print("="*50)
print("Salary\t\tCommision\tTotal Salary")
print("="*50)
for sal,comm,tsal in zip(sallist,commlist,total):
    print("{}\t\t{}\t\t{}".format(sal,comm,tsal))
print("="*50)