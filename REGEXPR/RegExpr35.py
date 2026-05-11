# Write a python program which will extract mail id's from given file where file contains text data

import re

with open("std1.data","r") as fp:
    filedata = fp.read()
    mailids = re.findall(r"\S+@\S",filedata)
    namelist = re.findall("[A-Z][a-z]+",filedata)
    print("-"*50)
    print("\tName\t\tMail")
    print("-"*50)
    for n,m in zip(namelist,mailids):
        print(f'\t{n}\t\t{m}')
    print("-"*50)
