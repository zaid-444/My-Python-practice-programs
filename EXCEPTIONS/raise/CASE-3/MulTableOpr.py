from MulTableExcept import NegNumError,ZeroError

def mul(num):
    n = int(num)
    if n < 0:
        raise NegNumError
    elif n == 0:
        raise ZeroError
    else:
        print("-"*50)
        print("\tMul Table of {}".format(n))
        print("-"*50)
        for i in range(1,11):
            print("\t{} x {} = {}".format(n,i,n*i))
        print("-"*50)

