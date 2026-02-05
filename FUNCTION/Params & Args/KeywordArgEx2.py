# Program for Demonstrating Keyword Arguments

def dispstudinfo(sno,sname,marks,crs="PYTHON",cnt="INDIA"):
    print(f'{sno}\t{sname}\t{marks}\t{crs}\t{cnt}')

print("-"*50)
print("SNO\tNAME\tMARKS\tCOURSE\tCOUNTRY")
print("-"*50)
dispstudinfo(100,"Naresh",96) #Possitional arguments
dispstudinfo(sname="Suresh",marks=56,sno=101) # Keyword arguments
dispstudinfo(crs="JAVA",sno=102,sname="Trump",cnt="USA",marks=69)# Keyword arguments
print("-"*50)
