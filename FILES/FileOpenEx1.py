# Write a python program which demonstrate opning the file and properties of file

try:
    fp = open("zaid.data","r")
except:
    print("File does not exist")
else:
    print("File Opened successfully in Read Mode")
    print("Type of fp =",type(fp))
finally:
    print("-"*40)
    print("Finally Block")
    print("Is File Closed =",fp.closed)
    fp.close()
    print("-"*40)