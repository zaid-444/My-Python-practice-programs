from DivOperation import divop
from DivExcept import ZeroError

try:
    a = int(input("Enter First Value: "))
    b = int(input("Enter Second Value: "))

    try:
        res = divop(a,b)
    except ZeroError:
        print("\tDon't Enter Zero for Den..")
    else:
        print("Div ({}/{}) = {}".format(a,b,res))
    finally:
        print("Finally Block")
except ValueError:
    print("Don't Enter alnums,strs and symbols")