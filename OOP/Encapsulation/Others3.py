# This Program demonstrates Data Abstraction
from Account3 import Account

ac = Account()
print(ac.__dict__)
# ac.getaccdata() -- can't access, bcoz getaccdata() is encapsulated