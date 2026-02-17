def add():
    a,b = int(input("First Value: ")),int(input("Second Value: "))
    print(f'Addition {a} + {b} = {a+b}')

def sub():
    a,b = int(input("First Value: ")),int(input("Second Value: "))
    print(f'Substraction {a} - {b} = {a-b}')

def mul():
    a,b = int(input("First Value: ")),int(input("Second Value: "))
    print(f'Multiplication {a} x {b} = {a*b}')

def div():
    a,b = int(input("First Value: ")),int(input("Second Value: "))
    print(f'FloatDiv {a} / {b} = {a/b}')
    print(f'FloorDiv {a} // {b} = {a//b}')

def mod():
    a,b = int(input("First Value: ")),int(input("Second Value: "))
    print(f'Modulo {a} % {b} = {a%b}')

def exp():
    a,b = int(input("Enter Base: ")),int(input("Enter Power: "))
    print(f'Expon {a} ** {b} = {a**b}')