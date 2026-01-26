# Program for generating 1 to n Numbers where n is +VE

n = int(input("Enter How many numbers you want: "))

if n <= 0:
    print(f'{n} is invalid Input')
else:
    for i in range(1,n+1):
        print(i)