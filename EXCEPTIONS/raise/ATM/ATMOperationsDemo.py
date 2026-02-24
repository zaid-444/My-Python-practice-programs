from ATMMenu import menu
from ATMOperations import depost,withdraw,balenq
from ATMExcept import DepositError,InsuffBalError,WithdrawError

while True:
    menu()
    try:
        choice = int(input("Enter Your Choice: "))
        match choice:
            case 1:
                try:
                    depost()
                except DepositError:
                    print("Don't enter -VE or 0 amout to Deposit")
                except ValueError:
                    print("Don't Enter Charachters")
            case 2:
                try:
                    withdraw()
                except WithdrawError:
                    print("Don't enter -VE or 0 to amount to Withdraw")
                except InsuffBalError:
                    print("-"*30)
                    print("Insufficiant Balance")
                except ValueError:
                    print("Don't enter Charachters")
            case 3:
                balenq()
            case 4:
                print("Thank's for using our ATM...")
                print("Visit again")
                break
            case _:
                print("You enter Wrong Operation")
                print("Try again....")
    except ValueError:
        print("Don't enter strs, alnums,and symbols for choice:-try again")