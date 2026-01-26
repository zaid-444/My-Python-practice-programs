# write a python program which will find sum of squares of n natural numbers

n = int(input("Enter How Many squares Numbers Sum u want: "))

if n <= 0:
    print(f'{n} is invalid input')
else:
    s = 0
    for i in range(1,n+1):
        print(i*i)
        s = s + i*i
    else:
        print("-"*4)
        print(s)