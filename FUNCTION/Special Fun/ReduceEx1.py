# Write a python program which will accept list of numerical values and find there sum by using reduce function

import functools

def sum1(k,v):
    return k+v

print("Enter a list of values")
lst = [10,20,30,40,50]

add = functools.reduce(sum1, lst)

print("----------")
print("Sum =",add)
print("----------")