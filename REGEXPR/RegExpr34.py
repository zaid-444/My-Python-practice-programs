# Program for extracting Names and marks from the file

import re

try:
    with open("std.data","r") as fp:
        filedata = fp.read()
        namelist = re.findall("[A-Z][a-z]+",filedata)
        marklist = re.findall(r'\d+',filedata)
        print("-"*30)
        print("\tName\tMarks")
        print("-"*30)
        for m,n in zip(marklist,namelist):
            print(f'\t{n}\t{m}')
        print("-"*30)
except FileNotFoundError:
    print("File Does not Exist")