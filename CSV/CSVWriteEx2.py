# Program for adding Record to Existing CSV file by using csv.write()

import csv

with open("citizen.csv","a") as fp:
    record = [500,"Zaid","MP"]
    csvwo = csv.writer(fp)
    csvwo.writerow(record)
    print("Record Inserted Successfully")