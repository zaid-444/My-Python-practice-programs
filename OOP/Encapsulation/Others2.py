# This Program demonstrates Data Abstraction
from Account2 import Account

ac = Account()
print(ac.__dict__)
ac.getaccdata()
print("-"*50)
# print("Account Number =",ac.accno)
print("Account Holder =",ac.cname)
# print("Account Bal    =",ac.__bal)
# print("Account PIN    =",ac.__pin)
print("Branch Name    =",ac.bname)
print("-"*50)
