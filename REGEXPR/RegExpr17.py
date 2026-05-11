# Searching for all except upper case alphabates and digits only
import re

x = re.finditer("[^0-9A-Z]","aB@Llj3#$klJ23$2cd")

for res in x:
    print(f'Start Index: {res.start()}  End Index: {res.end()}  Value: {res.group()}')