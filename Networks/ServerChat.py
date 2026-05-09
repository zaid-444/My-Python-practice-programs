# b) Write a server side program in such a way that server side program must receive a msg from the client side program and give reply to the client side program

import socket

s = socket.socket()

s.bind(("localhost",8000))
s.listen(2)
print("Server is Ready to Chat")
print("-"*60)

while True:
    cs, ca = s.accept()
    cdata = cs.recv(1024).decode()
    print("Client msg:",cdata)
    sdata = input("\t\tServer msg: ")
    cs.send(sdata.encode())