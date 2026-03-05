# Program for Demonstrating Converting JSON File String Format Data into Dict Data

import json

jsonobj = '{"FN":"ZAID","LN":"SHAIKH","mail":"zaid@gmail.com","state":"MH"}'
print(jsonobj,type(jsonobj))
print("-----------------------------"*3)
d = json.loads(jsonobj)
print(d,type(d))
print("-----------------------------"*3)
for k,v in d.items():
    print("\t{} ---> {}".format(k,v))
print("-----------------------------"*3)