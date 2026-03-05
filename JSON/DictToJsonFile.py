# Program for Demonstrating Saving Dict Data into JSON File

import json

d = {"FN":"ZAID","LN":"SHAIKH","mail":"zaid@gmail.com","state":"MH"}
print(d,type(d))

print("-"*70)

# Saving Dict Data into Json file

with open("stud.json","w") as fp:
    json.dump(d,fp)
    print("Data Saved Successfully in json file")