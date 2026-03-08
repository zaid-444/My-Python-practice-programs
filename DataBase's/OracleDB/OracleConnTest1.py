# Program for Demonstrating Connection from Oracle db

import oracledb 

zaid = oracledb.connect("system/tiger@localhost/orcl")

print("Python Program Connect to Oracle")
print("type of zaid =",type(zaid)) # <class, oracledb.Connection>