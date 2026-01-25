# HW  program to generate all odd numbers within n

n = int(input("Enter number to generate Odd numbers within range: "))

if n < 0:
    print(f'{n} is Invalid input')
else:
    i = 1
    while i <= n:
        print(i)
        i += 2