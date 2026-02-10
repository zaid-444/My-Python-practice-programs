# Write a python program which will accept list of values from the keyboard and find max and minby using anonymous function with list comprehnsion (Without using max and min fun)

def zaidmax(lst):
    m = lst[0]
    for n in lst:
        if n > m:
            m = n
    return m

def zaidmin(lst):
    m = lst[0]
    for n in lst:
        if n < m:
            m = n
    return m

print("-"*50)
lst = [ int(val) for val in input().split() ]

maxv = lambda lst: zaidmax(lst)
minv = lambda lst: zaidmin(lst)

resmax = maxv(lst)
resmin = minv(lst)

print("-"*50)
print("From this =",lst)
print("-"*50)

print("Big Value is =",resmax)
print("Small Value is =",resmin)
print("-"*50)