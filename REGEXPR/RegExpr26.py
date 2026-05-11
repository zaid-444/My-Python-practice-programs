# Searching for Exactly one Z
import re

x = re.finditer("Z","AkZZaids@zZkmvbZZZ")

for res in x:
    print(f'Start Index: {res.start()}  End Index: {res.end()}  Value: {res.group()}')