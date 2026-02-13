# Write a python program which will accept employees list of +VE salary.    obtain those employee salaries which are ranging from 0 to 500 and give 10% hike.   give 20% hike to those employees whose salary ranging from 501 to 1000.     print the total salary of 10% hiked employess and 20% hiked employees (Max salary is 1000 and min Sal is 0)

import functools

print("Enter Employees Salaries")
salaries = [ int(sal) for sal in input().split() if 0 <= int(sal) <= 1000 ]

sal0_500 = list(filter(lambda sal: 0 <= sal <= 500, salaries))
sal501_1000 = list(filter(lambda sal: 501 <= sal <= 1000, salaries))

hksal0_500 = list(map(lambda sal: sal+sal*10/100, sal0_500))
hksal501_1000 = list(map(lambda sal: sal+sal*20/100, sal501_1000))

totsal0_500 = functools.reduce(lambda a,b: a+b, sal0_500)
tothksal0_500 = functools.reduce(lambda x,y: x+y, hksal0_500)

totsal501_1000 = functools.reduce(lambda p,q: p+q, sal501_1000)
tothksal501_1000 = functools.reduce(lambda i,j: i+j, hksal501_1000)

print("-"*60)
print("0 to 500 Old & Hike Salaries")
print("="*60)
print("Old Sal\t\tHike Sal")
print("="*60)
for old,hik in zip(sal0_500,hksal0_500):
    print("{}\t\t{}".format(old,hik))
print("-"*40)
print("{}\t\t{}".format(totsal0_500,tothksal0_500))
print("*"*60)

print("501 to 1000 Old & Hike Salaries")
print("="*60)
print("Old Sal\t\tHike Sal")
print("="*60)
for old,hik in zip(sal501_1000,hksal501_1000):
    print("{}\t\t{}".format(old,hik))
print("-"*40)
print("{}\t\t{}".format(totsal501_1000,tothksal501_1000))
print("*"*60)