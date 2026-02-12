# Write a python program which will multiply two list objects

print("Enter List 1 Elements")
lst1 = [ int(val) for val in input().split() ]
print("Enter List 2 Elements")
lst2 = [ int(val) for val in input().split() ]

mul = list(map(lambda ls1,ls2: ls1*ls2,lst1,lst2))

print("="*50)
print("Num1\t\tNum2\t\tMul")
print("="*50)
for n1,n2,m in zip(lst1,lst2,mul):
    print("{}\t\t{}\t\t{}".format(n1,n2,m))
print("="*50)