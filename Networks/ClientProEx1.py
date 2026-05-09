# b) Write a Client side program in such a way that it must read a number from key Board, send to server side Program and get it's square from server side program.

import socket

s = socket.socket()
s.connect(("localhost",9999))

n = input("Enter a Number for Finding it's Square: ")
s.send(n.encode())

result = s.recv(1024).decode()

print("Square of {} = {}".format(n,result))