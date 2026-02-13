# Write a python program which will accept list of numerical values find the min by using reduce function

import functools

print("Enter list of values separated by space")
lst = [ int(val) for val in input().split() ]

def minfun(k,v):
    if k < v:
        return k
    else:
        return v

minv = functools.reduce(minfun,lst)

print("-"*50)
print("List of Values =",lst)
print("Min Number =",minv)
print("-"*50)