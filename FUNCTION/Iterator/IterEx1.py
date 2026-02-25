# Program for demonstrating Iterator

x = ["Zaid",444,"NXT","Python","Django"]
print(x)

itobj = iter(x)
print("type of itobj =",type(itobj))

print(next(itobj))

while True:
    try:
        print(next(itobj))
    except StopIteration:
        break