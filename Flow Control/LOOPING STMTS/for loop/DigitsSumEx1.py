# Write a Python Program which will find sum of the digits of the given number

num = int(input("Enter a Number: "))

tn = num
total = 0

while num > 0:
    d = num%10
    total = total+d
    num = num//10
else:
    print(f'The sum of {tn} = {total}')