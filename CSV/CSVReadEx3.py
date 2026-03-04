import csv

filename = input("Enter csv File Name: ")

with open(filename) as fp:
    csvro = csv.reader(fp)
    print("-"*40)
    for i in csvro:
        for j in i:
            print(j,end="\t")
        print()
    print("-"*40)