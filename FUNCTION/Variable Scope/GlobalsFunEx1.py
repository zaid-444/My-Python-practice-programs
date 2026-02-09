# Program for Demonstrating globals

a = 10
b = 20
c = 30
d = 40

def operation():
    a = 100
    b = 200
    c = 300
    d = 400
    res = a+b+c+d+globals()['a']+globals()['b']+globals()['c']+globals()['d']
    print("Sum =",res)

operation()