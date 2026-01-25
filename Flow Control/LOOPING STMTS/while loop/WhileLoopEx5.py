# Write a python program which will generate Even numbers in decreasing order

n = int(input("Enter number to generate Even numbers within range: "))

if n <= 0:
    print(f'{n} is Invalid input')
else:
    n = n if n%2 == 0 else n-1
    while n >= 2:
        print(n)
        n -= 2