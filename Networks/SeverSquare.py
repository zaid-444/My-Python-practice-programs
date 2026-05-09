# Write a python program which will implement the following

# a) Write a server side program in such way tha it should get a number from client side program square it and gives Square of that number as a result to client side program.

# b) Write a Client side program in such a way that it must read a number from key Board, send to server side Program and get it's square from server side program.

import socket

s = socket.socket()
s.bind(("localhost",9999))
s.listen(2)
print("SSP is ready to Accept any CSP Request")

while True: 
    try:
        cs,ca = s.accept()
        cdata = cs.recv(1024).decode()
        print("Client Data at Server Side =",cdata)
        cval = float(cdata)
        res = cval**2
        cs.send(str(res).encode())
    except ValueError:
        cs.send("Don't enter alnums,strs and symbols".encode())