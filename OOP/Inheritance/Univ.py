class Univ:
    def getUnivDet(self):
        self.uname = input("Enter University Name: ")
        self.uloc = input("Enter University Location: ")
    def dispUniDet(self):
        print("-"*50)
        print("\tUniversity Name: {}".format(self.uname))
        print("\tUniversity Location: {}".format(self.uloc))