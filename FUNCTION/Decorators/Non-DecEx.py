def val():
    return 5

def sqr():
    n = val()
    res = n ** 2
    print("Square of {} = {}".format(n,res))

def cube():
    n = val()
    res = n ** 3
    print("Cube of {} = {}".format(n,res))

def sqrt():
    n = val()
    res = n ** 0.5
    print("Square Root of {} = %0.2f".format(n) %res)

sqr()
cube()
sqrt()