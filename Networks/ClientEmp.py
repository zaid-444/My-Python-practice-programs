import socket

s = socket.socket()

s.connect(("localhost",8000))
print("Connected")
eno = input("Enter Employee Number: ")
s.send(eno.encode())

empdata = s.recv(1024).decode()
print("-"*50)
print("Employee Details")
print("-"*50)
print(empdata)
print("-"*50)