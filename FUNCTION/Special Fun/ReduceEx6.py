# Write a python program which will accept list of numerical values and find sum of +VE numerical values and -VE numerical values by using special funtion in python

import functools

print("Enter list of values separated by space")
lst = [ int(val) for val in input().split() ]

poslst = list(filter(lambda v: v>0, lst))
neglst = list(filter(lambda v: v<0, lst))

sumpos = functools.reduce(lambda a,b: a+b, poslst)
sumneg = functools.reduce(lambda a,b: a+b, neglst)

print("-"*60)
print("All Values =",lst)
print("+VE SUM =",sumpos)
print("-VE SUM =",sumneg)
print("-"*60)
