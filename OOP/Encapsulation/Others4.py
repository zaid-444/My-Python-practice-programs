# This Program will not work bcoz Account Class Encapsulated

from Account4 import Account

ac = Account()
ac.getaccdata()

print("-"*50)
print("Account Number =",ac.accno)
print("Account Holder =",ac.cname)
print("Account Bal    =",ac.bal)
print("Account PIN    =",ac.pin)
print("Branch Name    =",ac.bname)
print("-"*50)
