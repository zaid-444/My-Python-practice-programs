from NameExcept import NameValidError,ZeroLenError
from NameValidOpr import namevalidpro

name = input("Enter Ur Name: ")
try:
    res = namevalidpro(name)
except NameValidError:
    print("Invalid Name --- Try again")
except ZeroLenError:
    print("Name Must contain one char")
else:
    print(res)