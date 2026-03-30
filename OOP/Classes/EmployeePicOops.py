from Employee import Employee
import pickle

class EmployeePic:
    def saveemp(self):
        with open("emp.data","ab") as fp:
            while True:
                print("-"*50)
                eno = int(input("Enter Employee Number: "))
                name = input("Enter Employee Name: ")
                sal = float(input("Enter Employee Salary: "))
                print("-"*50)
                eo = Employee()
                eo.getempdata(eno,name,sal)
                pickle.dump(eo,fp)
                print("Employee Data Saved Successfully in File")
                print("-"*50)
                ch = input("Do u want to add another Employee(yes/no): ")
                if ch.lower() == 'no':
                    print("Thanks for using this program")
                    break

emp = EmployeePic()
emp.saveemp()