try:
    with open("zaid1.data","r+") as fp:
        print("File Created and Opened in Read Mode")
        print("File Name :",fp.name)
        print("File Mode :",fp.mode)
        print("Is File Readable =",fp.readable())
        print("Is File Writeable =",fp.writable())
        print("Is File Closed =",fp.closed)
except FileNotFoundError:
    print("File Does not Exist")