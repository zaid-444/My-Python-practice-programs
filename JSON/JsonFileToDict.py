# Program for Demonstrating Loading JSON File data into Dict Data

import json

with open("stud.json") as fp:
    data = fp.read()
    print(data,type(data))
    fp.seek(0)
    d = json.load(fp)
    print(d,type(d))