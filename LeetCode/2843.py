# Count Symmetric Integers

def func(low,high):
    c = 0
    for x in range(low,high+1):
        s = str(x)
        if len(s)%2 == 0:
            a = len(s) // 2
            fhalf = sum([ int(d) for d in s[:a]])
            shalf = sum([ int(d) for d in s[a:]])
            if fhalf == shalf:
                c += 1
    return c


low = int(input("Enter low value: "))
high = int(input("Enter high value: "))
print("~"*20)
print("Output:",func(low,high))
print("~"*20)