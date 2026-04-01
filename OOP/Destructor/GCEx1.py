print("Program Start")
print("-"*50)

import gc

print("Initially, Is GC Running =",gc.isenabled())

a = 10
b = 20
print("a =",a)
print("b =",b)

gc.disable()
print("Is GC Running after disable() =",gc.isenabled())

c = a + b
print("c =",c)
print("-"*50)
print("Program Finished")