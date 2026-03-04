# Program for creating CSV file with Dict data by using csv.DictWrite()

import csv

with open("teachers.csv",'a') as fp:
    header = ["TID","NAME","EXP","SUB"]
    records = [{"TID":100,"NAME":"Saloni","EXP":10,"SUB":"NURSING"},
               {"TID":101,"NAME":"Rahi","EXP":13,"SUB":"JAVA"},
               {"TID":102,"NAME":"Katrina","EXP":11,"SUB":"HEROINE"}]
    dictwo = csv.DictWriter(fp,fieldnames=header)
    dictwo.writeheader()
    dictwo.writerows(records)
    print("CSV file created..")

print("Is closed =",fp.closed)