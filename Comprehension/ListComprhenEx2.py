# Write a python program which will accept only +VE numbers from list of mixed numerical values 

print("Enter list of values")

plst = [ int(val) for val in input().split() if int(val) > 0 ]
print("List of +VE values =",plst)

nlst = [ int(val) for val in input().split() if int(val) < 0 ]
print("List of -VE values =",nlst)