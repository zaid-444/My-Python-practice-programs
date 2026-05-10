import re

s = "Python is an oop lang.Python is also fun prog lang"
sp = "Python"

l = re.findall(sp,s)
print(l)
print("Number of times {} found = {}".format(sp,len(l)))