# Program for Cal div of Two Numbers
try:
    print("Program Started")
    s1 = input("Enter First Value: ")
    s2 = input("Enter Second Value: ")

    a = int(s1) # Generates----ValueError
    b = int(s2)  # Generates----ValueError
    c = a / b   # Generates-----ZeroDivisionError
except ZeroDivisionError:
    print("\tYou Can't Divide number with Zero")
except ValueError:
    print("\tDon't Enter Symbols,Alphanums and STRS")
else:
    print("---------------else---------------")
    print("Div = %0.2f" %c)
    print("----------------------------------")
finally:
    print("Program Ended")