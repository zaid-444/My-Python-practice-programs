# Program for demonstrating Generator

def zaidrange(start,stop,step=1):
    while start <= stop:
        yield start
        start += step


go = zaidrange(10,50,10)

for val in go:
    print(val)

print("-"*40)

go1 = zaidrange(100,110,3)

while True:
    try:
        print(next(go1))
    except StopIteration:
        break

print("-"*40)

go2 = zaidrange(1,10)
for val in go2:
    print(val)