# Searching for all except alpha-numeric values

import re

x = re.finditer("[^0-9a-zA-Z]","aB@Llj3#$klJ23$2cd")

for res in x:
    print(f'Start Index: {res.start()}  End Index: {res.end()}  Value: {res.group()}')