# Program for Reading CSV file data

import csv

with open("D:\Python NareshIT(2024) KV Rao sir\Problems\CSV\emp.csv") as fp:
    csvro = csv.reader(fp)
    for i in csvro:
        print("-"*40)
        for j in i:
            print(j,end="\t")
        print()
    print("-"*40)