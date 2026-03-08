import oracledb as ordb

try:
    con = ordb.connect("system/tiger@127.0.0.1/orcl")
    print("Connected to Oracle")
except ordb.DatabaseError as db:
    print(db)