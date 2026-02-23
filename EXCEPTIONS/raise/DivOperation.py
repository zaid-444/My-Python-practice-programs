from DivExcept import ZeroError

def divop(a,b):
    if b == 0:
        raise ZeroError # riase is hitting or raising the exception
    else:
        return a / b