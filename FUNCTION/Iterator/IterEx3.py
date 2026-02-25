# Program for demonstrating Iterator

x = {"Zaid",444,"NXT","Python","Django"}
print(x)

itobj = iter(x)
print("type of itobj =",type(itobj))
print("="*50)

print(next(itobj))
print("-"*10)
while True:
    try:
        print(next(itobj))
    except StopIteration:
        break