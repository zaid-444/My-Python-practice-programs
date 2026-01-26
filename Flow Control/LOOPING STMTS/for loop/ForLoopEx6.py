# write a python program which will find sum of natural number

n = int(input("Enter How Many Natural Numbers Sum u want: "))

if n <= 0:
    print(f'{n} is invalid input')
else:
    total = 0
    for i in range(1,n+1):
        print(i)
        total += i
    else:
        print("-"*5)
        print(total)
        print("-"*5)