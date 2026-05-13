def smallEvenMUl(n):
    if n%2 == 0:
        return n
    else:
        return n * 2
    
n = int(input("Enter Value of N: "))

print("-"*40)
print("Smalles Even Multiple of: {} = {}".format(n,smallEvenMUl(n)))
print("-"*40)