# Searching for all except 'a' or 'b' or 'c' only

import re

x = re.finditer("[^abc]","aB@lkj3#$klj23$2cd")

for res in x:
    print(f'Start Index: {res.start()}  End Index: {res.end()}  Value: {res.group()}')