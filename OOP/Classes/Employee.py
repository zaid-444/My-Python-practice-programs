class Employee:
    def getempdata(self,eno,ename,sal):
        self.eno = eno
        self.ename = ename
        self.sal = sal
    
    def disemp(self):
        print("\t{}\t{}\t{}".format(self.eno,self.ename,self.sal))