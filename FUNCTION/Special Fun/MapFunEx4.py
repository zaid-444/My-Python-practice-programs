# Write a python program which will accept list of numerical values and find there squares and sqare root

print("Enter a list of values separated by space")

lst = [ int(val) for val in input().split() ]

sqr = list(map(lambda num: num**2,lst))
sqrt = list(map(lambda num: num**0.5,lst))

print("="*50)
print("Number\t\tSquare\tSquare Root")
print("="*50)
for num,s,sqt in zip(lst,sqr,sqrt):
    print("{}\t\t{}\t %0.2f".format(num,s) %sqt)

print("="*50)