# Write a python program which will axtract names of the students from the given text by using RegExpr

import re 

data = "Rossum is the father of python, Rohit is the father of cricekt, Ronaldo is the father of  football"

sp = "[A-Z][a-z]+"

nameslist = re.findall(sp,data)

print("List of Names")
print("-"*40)
for names in nameslist:
    print(f"\t{names}")
print("-"*40)