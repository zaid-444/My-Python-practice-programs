import Menu
from Operations import add,sub,mul,div,mod,exp

Menu.menu()

while True:
    n = int(input("Enter your Operation: "))
    match n:
        case 1:
            add()
            print("-"*50)
        case 2:
            sub()
            print("-"*50)
        case 3:
            mul()
            print("-"*50)
        case 4:
            div()
            print("-"*50)
        case 5:
            mod()
            print("-"*50)
        case 6:
            exp()
            print("-"*50)
        case 7:
            print("Thanks for using our Caculator")
            print("-"*50)
            break
        case _:
            print("Ivalide Input")
            print("-"*50)