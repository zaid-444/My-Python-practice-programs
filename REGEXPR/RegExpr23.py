# Searching for all except alpha-numeric
import re

x = re.finditer(r"\W","aB@Llj3#$kl J23$2cd")

for res in x:
    print(f'Start Index: {res.start()}  End Index: {res.end()}  Value: {res.group()}')