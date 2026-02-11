# Write a python program which will accept list of words and obtain only palendrome words

print("Enter list of Values separated by space")

lst = [ val for val in input().split() ]

palinword = list(filter(lambda word: word==word[::-1], lst))

print("*"*50)
print("Content of list =",lst)
print("Palindrome list =",palinword)
print("*"*50)