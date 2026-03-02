# Write a python program which will display content of any file

try:
    filename = input("Enter File Name: ")
    with open(filename,"rt") as fp:
        filedata = fp.readlines()
        print("-"*50)
        for line in filedata:
            print(line,end="")
        print("-"*50)
except FileNotFoundError:
    print("File Not Exist")