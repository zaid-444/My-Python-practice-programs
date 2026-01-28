# Write a python program which will accept a numeric value and decide whether it is prime number or not

n = int(input("Enter a Number to decide Prime or Not: "))

if n <= 0:
    print("{} is invalid input".format(n))
else:
    for i in range(2,n):
        if n%i == 0:
            print("{} is not Prime".format(n))
            break
    else:
        print("{} is Prime".format(n))