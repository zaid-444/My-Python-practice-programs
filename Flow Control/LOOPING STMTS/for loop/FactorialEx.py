# Write a python Program Which will find Factorial of Given Number

n = int(input("Enter a number to find factorial: "))

if n < 0:
    print(f"{n} is invalid input")
elif n == 0 or n == 1:
    print(f"Factorial of {n} is 1")
else:
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    else:
        print(f"Factorial of {n} = {fact}")

        

print("="*50)



n = int(input("Factorial using while, Enter n: "))

if n < 0:
    print(f'{n} factorial not exist')
elif n == 0 or n == 1:
    print('Factorial of {n} = 1')
else:
    i = 1
    fact = 1
    while i <= n:
        fact = fact*i
        i += 1
    else:
        print(f'Factorial of {n} = {fact}')