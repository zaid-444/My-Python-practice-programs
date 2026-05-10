# Searching for either 'a' or 'b' or 'c' only

import re

x = re.finditer("[abc]","aBA@lkj35#$kljblkj23$2cd")

for res in x:
    print(f'Start Index: {res.start()}  End Index: {res.end()}  Value: {res.group()}')