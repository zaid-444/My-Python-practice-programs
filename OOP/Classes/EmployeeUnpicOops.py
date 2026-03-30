import pickle

class EmployeeUnpic:
    def readrecord(self):
        try:
            print("-"*50)
            with open("emp.data","rb") as fp:
                while True:
                    try:
                        record = pickle.load(fp)
                        record.disemp()
                    except EOFError:
                        print("-"*50)
                        break
        except FileNotFoundError:
            print("File Does Not Exists")

emp = EmployeeUnpic()
emp.readrecord()