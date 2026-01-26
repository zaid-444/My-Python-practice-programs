# Write a Python Program which will find sum of the digits of the given number Using another Method

num = input("Enter any number: ")

t = 0

for i in num:
    t += int(i)

print(f'Sum of {num} = {t}')