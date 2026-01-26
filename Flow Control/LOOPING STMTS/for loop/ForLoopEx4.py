# write a python program which will generate all even numbers within n where n is +VE using for loop

n = int(input("Enter a end number to generate upto there even number: "))

if n <= 0:
    print(f'{n} is invalid input')
else:
    for i in range(2,n+1,2):
        print(i)