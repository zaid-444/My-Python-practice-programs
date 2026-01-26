# Program for Finding Product of N Natural Numbers where N is +VE

n = int(input("enter the Value of N for finding its product: "))

if n <= 0:
    print(f'{n} is invalid input')
else:
    s = 1
    for i in range(1,n+1):
        s = s*i
    else:
        print(f'Product of {n} numbers = {s}')