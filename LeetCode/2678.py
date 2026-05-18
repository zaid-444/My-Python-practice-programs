# 2678. Number of Senior Citizens

def countSeniors(details):
    snrctzn = 0
    for det in details:
        if int(det[11:13]) > 60:
            snrctzn += 1
    print("Cenior Citizens =",snrctzn)

details = [ detail for detail in input("Enter Details: ").split() ]
countSeniors(details)