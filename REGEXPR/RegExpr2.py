import re

s = "python is an oop lang.Python is also fun prog lang"
sp = "Python"

res = re.search(sp,s)

if res!= None:
    print("Search is Successful")
    print("---------------------")
    print("Start Index =",res.start())
    print("End Index =",res.end())
    print("Value =",res.group())
    print("---------------------")
else:
    print("Search is Un-Successful")