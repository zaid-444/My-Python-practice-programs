# program for Creating csv file by using csv.writer()

import csv

with open("citizen.csv","a") as fp:
    hnames = ["CID","NAME","STATE"]
    records = [[100,"Naresh","TS"],[200,"Ramesh","AP"],[300,"Suresh","MH"],[400,"Salman","HR"]]
    csvwro = csv.writer(fp)
    csvwro.writerow(hnames)
    csvwro.writerows(records)
    print("CSV File Created")