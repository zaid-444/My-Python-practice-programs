# Write a python program which will retrive marks of the students from the given text

import re

data = "Zaid got 98 marks, Rohit got 45 marks, Virat got 18 marks, Raahi got 100 marks"

# sp = "[0-9]+"
sp = r"\d+"
np = "[A-Z][a-z]+"

markslist = re.findall(sp,data)
namelist = re.findall(np,data)

print("-"*30)
print("\tName\tMarks")
print("-"*30)
for mark,name in zip(markslist,namelist):
    print(f'\t{name}\t{mark}')
print("-"*30)