# Write a python program which will generate multiplication table for a given +VE int Valuef

mul_num = int(input("Enter a number to generate multiplication Table: "))

if mul_num < 0:
    print(f'{mul_num} is invalid input')
else:
    n = 1
    while n <= 10:
        print(f'{mul_num}x{n}={mul_num*n}')
        n += 1