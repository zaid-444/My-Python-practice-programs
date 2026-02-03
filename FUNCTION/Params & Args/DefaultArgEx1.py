# Program for Demonstrating Default Arguments or Params

def studinfo(sno,sname,marks,crs="PYTHON"):
    print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

print("="*50)
print("\tSNO\tNAME\tMARKS\tCOURSE")
print("="*50)
studinfo(100,"Naresh",88)
studinfo(200,"Suresh",56)
studinfo(300,"Ramesh",69)
studinfo(400,"Kishor",46,"JAVA")
print("="*50)