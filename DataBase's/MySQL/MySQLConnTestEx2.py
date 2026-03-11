import mysql.connector

try:
    con = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        passwd = "zaid0444"
    )
    print("Connected Successfully")
except mysql.connector.Error as db:
    print("Error: ",db)