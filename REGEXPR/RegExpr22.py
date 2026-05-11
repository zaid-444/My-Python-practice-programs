# Searching for all alpha-numeric
import re

x = re.finditer(r"\w","aB@Llj3#$klJ23$2cd")

for res in x:
    print(f'Start Index: {res.start()}  End Index: {res.end()}  Value: {res.group()}')