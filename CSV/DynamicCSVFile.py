# Write a python program which will create dynamic csv file

import csv

filename = input("Enter CSV File name: ")
h = int(input("Ente how many header name u want to enter in {} file: ".format(filename)))

if h <= 0:
    print("Atleast 1 header Require but u enter {}".format(h))
else:
    colnames = []
    for i in range(1,h+1):
        col = input("Enter Col name {}: ".format(i))
        colnames.append(col)
    else:
        r = int(input("Enter how many records u want to enter: "))
        if r <= 0:
            print("{} invalide input".format(r))
        else:
            records = []
            for i in range(1,r+1):
                print("-"*30)
                print("Enter Record no. {}: ".format(i))
                record = []
                for j in range(len(colnames)):
                    val = input("Enter Value for {}: ".format(colnames[j]))
                    record.append(val)
                else:
                    records.append(record)
            else:
                with open(filename,"a") as fp:
                    wo = csv.writer(fp)
                    wo.writerow(colnames)
                    wo.writerows(records)
                    print("{} Created succefully".format(filename))