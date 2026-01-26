# Write a python program which will read list of values from keyboard and display thos values

nov = int(input("How many value you want to Enter: "))

if nov <= 0:
    print("{} is Invalid input".format(nov))
else:
    lst = []
    for v in range(1,nov+1):
        v = float(input("Enter value no.{}: ".format(v)))
        lst.append(v)

print("You Entered Values are = {}".format(lst))