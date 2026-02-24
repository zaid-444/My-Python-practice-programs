from MulTableOpr import mul
from MulTableExcept import NegNumError,ZeroError

while True:
    try:
        num = input("Enter any Number: ")
        mul(num)
    except ValueError:
        print("Don't Enter alnums,strs,floats and special symbols")    
    except NegNumError:
        print("Don't Enter -VE Number")
    except ZeroError:
        print("For 0 Multiplication Table not Exist")
    else:
        print("Thnx for using program")
        break