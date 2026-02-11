# Program for Filtering +VE and -VE Values from list of Values

print("Enter list of Values separated by space")

lst = [int(val) for val in input().split() ]
print("-"*50)
print("List of Values =",lst)
print("-"*50)

pos = list(filter(lambda num: num>0, lst))
neg = list(filter(lambda num: num<0, lst))
print("+VE numbers =",pos)
print("-VE numbers =",neg)
print("-"*50)