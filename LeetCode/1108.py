# 1108. Defanging an IP Address

def defangIPaddr():
    addr = input("Enter a Valid(IPv4) IP address: ")
    return addr.replace(".","[.]")

res = defangIPaddr()
print("-"*50)
print("Result is =",res)