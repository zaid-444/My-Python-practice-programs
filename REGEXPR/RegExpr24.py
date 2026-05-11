# Searching for Space Characters only
import re

x = re.finditer(r"\s","aB@ Llj3#$kl J23$2cd")

for res in x:
    print(f'Start Index: {res.start()}  End Index: {res.end()}  Value: {res.group()}')