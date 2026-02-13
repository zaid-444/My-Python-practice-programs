# Write a python program which will accept list of numerical values and find there sum by using reduce function

import functools

print("Enter list of values")

lst = [ int(val) for val in input().split() ]

res = functools.reduce(lambda k,v: k+v, lst)

print("-"*30)
print("Sum =",res)
print("-"*30)