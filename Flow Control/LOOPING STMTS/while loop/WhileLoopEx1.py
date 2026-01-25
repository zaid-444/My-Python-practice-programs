# Write a python program which will generate 1 to n numbers where n is positive

n = int(input("Enter how many numbers you want: "))

if n < 0:
    print("{} is Invalide number".format(n))
else:
    i = 1
    while i <= n:
        print(i)
        i += 1
    else:
        print("I am from else part of while loop")