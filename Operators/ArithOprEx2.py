# Program for Demonstrating Square Root of given Number without using sqrt() of math module

num = int(input("Enter any Number for cal Square Root of a Number: "))

res = num**0.5 # OR res = num ** (1/2)

print("Sqrt ({}) = {}".format(num,round(res,2)))