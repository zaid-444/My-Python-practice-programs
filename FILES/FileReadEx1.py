# Program for Demonstrating Reading the Data from the file

try:
    with open("info.data") as fp:
        filedata = fp.read()
        print("-"*50)
        print(filedata)
        print("-"*50)
except FileNotFoundError:
    print("File does not Exist")