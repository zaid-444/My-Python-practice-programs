# Program for demonstrating Iterator

x = ("Zaid",444,"NXT","Python","Django")
print(x)

itobj = iter(x)
print("type of itobj =",type(itobj))

print(next(itobj))
print()
for val in itobj:
    print(val)