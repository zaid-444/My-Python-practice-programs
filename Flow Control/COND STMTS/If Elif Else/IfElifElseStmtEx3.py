# Program for accepting a Digit and display Digit Name

d = int(input("Enter any Digit: "))

dobj = {0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}

# if dobj.get(d) == None:
#     print("{} is Number".format(d))

# else:
#     print("{} is {}".format(d,dobj.get(d)))

res = "{} is Number".format(d) if dobj.get(d) == None else "{} is {}".format(d,dobj.get(d))

print(res)