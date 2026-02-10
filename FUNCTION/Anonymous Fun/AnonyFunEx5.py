# Write a python program which will accept list of values from the keyboard and find max and min by using anonymous function with list comprehnsion

minv = lambda lst: min(lst)
maxv = lambda lst: max(lst)

lst = [ int(val) for val in input().split() ]

resmax = maxv(lst)
resmin = minv(lst)

print("-"*50)
print("From this list =",lst)
print("-"*50)
print("Min Value =",resmin)
print("Max Value =",resmax)
print("-"*50)
