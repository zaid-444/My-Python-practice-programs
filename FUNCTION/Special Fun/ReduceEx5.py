# Write a python program which will accept list of words and obtain a single line of text by using reduce function (It should work like a join fun)

import functools

print("Enter line of text separated by space")
text_line = [ word for word in input().split() ]

res = functools.reduce(lambda i,j: i + ' ' + j, text_line)

print("-"*60)
print("List of words =",text_line)
print("Result =",res)
print("-"*60)