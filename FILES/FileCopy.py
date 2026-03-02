# Write a python program which will copy the content of one file into another file

srcfile = input("Enter name of Source File: ")

try:
    with open(srcfile,"r") as srp:
        filedata = srp.read()
        copyfile = input("Enter in which file you want to copy: ")
        with open(copyfile,"a") as desp:
            desp.writelines(filedata)
            print("Data Copied Successfully")
except FileNotFoundError:
    print("File Not Exist")