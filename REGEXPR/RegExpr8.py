# Searching for all upper case alphabats

import re

x = re.finditer("[A-Z]","aB@Llj3#$klJ23$2cd")

for res in x:
    print(f'Start Index: {res.start()}  End Index: {res.end()}  Value: {res.group()}')