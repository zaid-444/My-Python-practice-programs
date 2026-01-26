# write a python program which will gnerate multiplication table using for loop

n = int(input("Enter a Number in which we generate Mul table: "))

if n <= 0:
    print(f"{n} is invalid input")
else:
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')