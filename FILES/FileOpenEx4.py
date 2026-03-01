
with open("zaid1.data","w") as fp:
    print("File Created and Opened in Write Mode")
    print("File Name :",fp.name)
    print("File Mode :",fp.mode)
    print("Is File Readable =",fp.readable())
    print("Is File Writeable =",fp.writable())
    print("Is File Closed =",fp.closed)