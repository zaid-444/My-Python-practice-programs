# Write a python program which will accept number of employee details such as employee no. employee name salary designation and save as a record in file by using Pickling concept

import pickle

def emp():
    with open("emp.data","ab") as fp:
        while True:
            try:
                print("*"*52)
                eno = int(input("Enter Employee Number: "))
                ename = input("Enter Employee Name: ")
                sal = float(input("Enter Employee Salary: "))
                dsg = input("Enter Designation: ")
                print("*"*52)
                lst = []
                lst.append(eno)
                lst.append(ename)
                lst.append(sal)
                lst.append(dsg)
                pickle.dump(lst,fp)
                print("Employee Record Saved in a file Successfully")
                print("*"*52)
                n = input("Do u Want to enter another emp Yes/No: ")
                if n.lower() == "no":
                    break
            except ValueError:
                print("Don't Enter Wrong Data try again...")

emp()