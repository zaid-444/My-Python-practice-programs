# Program for Reading the Values from KBD and find squares by using Dict Comprehension

print("Enter List of Values separated by comma.")

dct = {int(val):int(val)**2 for val in input().split(",")}
print("-"*50)
print("\tNumber\tSquares")
print("-"*50)
for n,s in dct.items():
    print("\t{}\t{}".format(n,s))
print("-"*50)