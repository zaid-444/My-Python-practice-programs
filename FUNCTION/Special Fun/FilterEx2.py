# Program for Filtering +VE and -VE Values from list of Values using ano fun

print("Enter list of Values separated with space")

lst = [10,-20,30,0,-66,52,0,-44,24]
print("-"*50)
print("List of Values =",lst)
print("-"*50)

pos = list(filter(lambda num: num>0, lst))
neg = list(filter(lambda num: num<0, lst))
print("+VE numbers =",pos)
print("-VE numbers =",neg)
print("-"*50)