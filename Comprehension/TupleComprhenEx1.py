# Program for Reading the Values from KBD by using set comprehension

print("Enter List of Values:")

x = (int(val) for val in input().split()) # x is generator
print("Content of x =",x)
print("-"*50)

tpl = tuple(x)
print("Content of tpl =",tpl)
print("Type of tpl =",type(tpl))