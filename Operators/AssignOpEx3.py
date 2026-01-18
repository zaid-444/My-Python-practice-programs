# Program for Swapping Two Integer Values 

a,b = int(input("Enter Integer Value of a: ")),int(input("Enter Integer Value of b: "))

 
print("*"*40)

print("\tOriginal Value of a:{}".format(a))
print("\tOriginal Value of b:{}".format(b))
print("*"*40)

a = a + b
b = a - b
a = a - b

print("\tSwapped Value of a:{}".format(a))
print("\tSwapped Value of b:{}".format(b))


print("*"*40)