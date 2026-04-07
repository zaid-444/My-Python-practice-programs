from Univ import Univ
class College(Univ):
    def getColDet(self):
        self.cname = input("Enter College Name: ")
        self.cloc = input("Enter College Location: ")
    def dispColDet(self):
        print("-"*50)
        print("\tCollege Name :",self.cname)
        print("\tCollege Location :",self.cloc)