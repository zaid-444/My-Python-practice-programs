# Program for Demonstrating Possitional Arguments
def studinfo(sno,sname,marks,crs): # Here sno,sname,marks,crs are called Possitional Parameter
    print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs))

print("="*50)
print("\tSNO\tNAME\tMARKS\tCOURSE")
print("="*50)
studinfo(100,"Naresh",88,"PYTHON")
studinfo(200,"Suresh",56,"PYTHON")
studinfo(300,"Ramesh",69,"PYTHON")
studinfo(400,"Kishor",46,"PYTHON")
print("="*50)