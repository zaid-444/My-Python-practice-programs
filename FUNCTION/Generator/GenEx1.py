# Program which demonstrates the need of Generator 

def zaidrange(val):
    i = 0
    while i < val:
        yield i
        i += 1
    
z = zaidrange(10)
print(type(z))
print(next(z))
print(next(z))
print(next(z))

while True:
    try:
        print(next(z))
    except StopIteration:
        break

print("-"*30)

x = zaidrange(5)

for val in x:
    print(val)