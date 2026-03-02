# Program for Demonstrating Reading the Data from the file

try:
    with open("zaid.data") as fp:
        filedata = fp.readlines()
        print("-"*50)
        for line in filedata:
            print(line,end="")
        print()
        print("-"*50)
except FileNotFoundError:
    print("File does not Exist")