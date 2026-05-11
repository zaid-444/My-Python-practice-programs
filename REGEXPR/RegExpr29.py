# Searching for zero Z or One Z's
import re

x = re.finditer("Z?","AkZZaiZkbZZZ")

for res in x:
    print(f'Start Index: {res.start()}  End Index: {res.end()}  Value: {res.group()}')