# Write a python program which will accept list of values from keyboard and find there sum and average

print('-'*50)
nov = int(input("How many value you want to Enter: "))
print('-'*50)

total = 0
lst = []

for i in range(1,nov+1):
    val = float(input(f'Enter Value {i}: '))
    total += val
    lst.append(val)

print('-'*50)
print("Sum = {}".format(total))
print("Average = {}".format(total/len(lst)))
print('-'*50)