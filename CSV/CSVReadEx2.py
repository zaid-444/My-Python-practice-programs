# Program for Reading CSV File data in the form of Dict Format.

import csv

try:
    with open("emp.csv") as fp:
        dictro = csv.DictReader(fp)
        for i in dictro:
            print("-"*40)
            for k,v in i.items():
                print("{} = {}".format(k,v))
        print("-"*40)
except FileNotFoundError:
    print("File Not Exist")