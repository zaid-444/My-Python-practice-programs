# Write a python program which will generate prime numbers within the given range

num = int(input("Enter the number to generate prime within range: "))

if num <= 1:
    print(f'{num} invalid input')
else:
    for i in range(2,num+1):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            print(i)