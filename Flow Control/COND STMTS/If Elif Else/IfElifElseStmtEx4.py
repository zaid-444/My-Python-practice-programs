# Program for accepting a Digit and display Digit Name

d = int(input("Enter any Number: "))

d_obj = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}

print("{} is {}".format(d,d_obj.get(d)) if d_obj.get(d) != None else ("{} is -VE Digit".format(d)) if d in range(-1,-10,-1) else ("{} is +VE Number".format(d)) if d>9 else ("{} is -VE Number").format(d))