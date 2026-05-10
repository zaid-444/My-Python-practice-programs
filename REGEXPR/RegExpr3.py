import re

s = "Python is an oop lang.Python is also fun prog lang"
sp = "Python"

res = re.finditer(sp,s)

print(type(res))

for i in res:
    print("---------------------")
    print("Start Index =",i.start())
    print("End Index =",i.end())
    print("Value =",i.group())

