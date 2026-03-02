# Write a python program which will display content of any file

file = input("Enter File name to see content: ")

try:
    with open(file,"r") as fp:
        filedata = fp.read()
        print("-"*50)
        print(filedata)
        print("-"*50)
except FileNotFoundError:
    print("File does not Exist")