# Searching for zero Z or One or More Z's
import re

x = re.finditer("Z*","AkZZaiZkmvbZZZ")

for res in x:
    print(f'Start Index: {res.start()}  End Index: {res.end()}  Value: {res.group()}')