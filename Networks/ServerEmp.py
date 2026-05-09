# Write a Client side program in such a way that it should accept the emp number from keyboard, send to server side program and obtain other details of employee from server side program

import socket,mysql.connector

s = socket.socket()
s.bind(("localhost",8000))
s.listen(2)

print("Server Side Program Ready to take request")

while True:
    try:
        cs,ca = s.accept()
        empno = int(cs.recv(1024).decode())
        
        con = mysql.connector.connect(host = "localhost",
                                    user = "root",
                                    password = "zaid0444",
                                    database = "test1")
        cur = con.cursor()
        cur.execute("select * from employee where eno=%d" %empno)
        record = cur.fetchone()

        if record == None:
            cs.send(f"Employee {empno} Not Exist".encode())
        else:
            eno = "Employee Number: " + str(record[0])
            ename = "Employee Name: " + str(record[1])
            empsal = "Employee Salary: " + str(record[2])
            ecomp = "Employee Company: " + str(record[3])
            cs.send(str(eno + "\n" + ename + "\n" + empsal + "\n" + ecomp).encode())
    except mysql.connector.DatabaseError:
        cs.send("Error in Database".encode())
    except ValueError:
        cs.send("Plz Provide Valide Employee Number".encode())