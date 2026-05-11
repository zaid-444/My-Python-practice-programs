# Searching for all except Space Characters
import re

x = re.finditer(r"\S","aB@ Llj3#$kl J23$2cd")

for res in x:
    print(f'Start Index: {res.start()}  End Index: {res.end()}  Value: {res.group()}')