# 10. Write a Python program to find the list of words that are longer than n from a given list of words.

print("Enter a list of values separated by space")

lst = [ word for word in input().split() ]
n = int(input("Enter Value of n: "))

lgn = []

for word in lst:
    if len(word) > n:
        lgn.append(word)

# lgn = [ word for word in lst if len(word) > n]

print("="*50)
print("List of words =",lst)
print("Value of N =",n)
print("="*50)
print("Longer than {} chr word of List".format(n))
print(lgn)
print("="*50)