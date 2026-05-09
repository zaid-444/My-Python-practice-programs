# b) Write a client side program in a such way that client sends a msg and get a reply for it

import socket
print("Server is Ready to Chat")
print("-"*60)


while True:
    s = socket.socket()
    s.connect(("localhost",8000))

    cdata = input("\t\tClient msg: ")
    if cdata == "@":
        print("Bye Client 🙈 have a good day")
        break
    else:
        s.send(cdata.encode())
        sdata = s.recv(1024).decode()
        print("Server msg:",sdata)