# Write a python program which will find max value from list of numbers by using reduce function

import functools

values = [ int(val) for val in input().split() ]

Max = functools.reduce(lambda k,v: k if k>v else v, values)

print("-"*50)
print("List of Values =",values)
print("Max is =",Max)
print("-"*50)