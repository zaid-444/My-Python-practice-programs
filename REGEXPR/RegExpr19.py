# Searching for all except lower case alphabates and digits only
import re

x = re.finditer("[^0-9a-z]","aB@Llj3#$klJ23$2cd")

for res in x:
    print(f'Start Index: {res.start()}  End Index: {res.end()}  Value: {res.group()}')