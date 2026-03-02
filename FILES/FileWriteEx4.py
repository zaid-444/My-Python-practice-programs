# Program for Demonstrating Writing the Data to the file

x = {"Python",1+2j,"Zaid","XYZ","XYZ"}

with open("stud.data","a") as fp:
    fp.writelines(str(x)+"\n")
    print("Data is Written Succussfully")