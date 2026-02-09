# Program for Reading the Values from KBD by using set comprehension

print("Enter List of Values:")
st = {int(val) for val in input().split()}
print("Content of st =",st)
print("Type of st =",type(st))