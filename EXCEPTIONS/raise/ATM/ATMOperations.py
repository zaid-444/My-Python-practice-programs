from ATMExcept import DepositError,InsuffBalError,WithdrawError

bal = 500

def depost():
    damt = int(input("Enter how much amount u want to Deposite: "))
    if damt <= 0:
        raise DepositError
    else:
        global bal
        bal += damt
        print("Ur a/c no.XXXXXX1234 is credited Rs.{}".format(damt))
        print("Ur a/c no.XXXXXX1234 current Bal Rs.{}".format(bal))

def withdraw():
    wamt = int(input("Enter How much amount u want to Withdraw: "))
    global bal
    if wamt <= 0:
        raise WithdrawError
    elif wamt+500 > bal:
        raise InsuffBalError
    else:
        bal = bal - wamt
        print("Ur a/c no.XXXXXX1234 is withdraw Rs.{}".format(wamt))
        print("Ur a/c no.XXXXXX1234 current Bal Rs.{}".format(bal))

def balenq():
    print("Ur a/c no.XXXXXX1234 current Bal Rs.{}".format(bal))