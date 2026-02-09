# Program for Demonstrating globals

a = 10
b = 20

def getglobalvals():
    a = 100
    b = 200
    d = globals() # d is dict type
    print("-"*50)
    print("invisible and user defined global variables")
    print("-"*50)
    for k,v in d.items():
        print("\t{}--->{}".format(k,v))
    print("-"*50)
    print("User-defined Global Variable way-1")
    print("-"*50)
    print("Global Var a = {}".format(d['a']))
    print("Global Var b = {}".format(d['b']))
    print("-"*50)
    print("User-defined Global Variable way-2")
    print("Global Var a = {}".format(d.get('a')))
    print("Global Var b = {}".format(d.get('b')))
    print("-"*50)



getglobalvals()