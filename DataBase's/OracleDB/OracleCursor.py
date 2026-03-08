# Program for Demonstrating to create an object of cursor

import oracledb as orc

con = orc.connect("system/tiger@localhost/orcl")
print("Connected to DataBase")

print("-"*50)

cur = con.cursor()
print("Cursor Object Created")