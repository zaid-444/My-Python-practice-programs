# Searching for all values
import re

x = re.finditer(".","AkZZaiZkbZZZ")

for res in x:
    print(f'Start Index: {res.start()}  End Index: {res.end()}  Value: {res.group()}')