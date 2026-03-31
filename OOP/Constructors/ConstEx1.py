# Program for Class and Objects with Constructors for Initilizing the Object

class Student:
    def __init__(self):
        print("I am From Constructor")
        self.rollno = 30
        self.name = "Zaid"

s = Student() # During the Object Creation PVM Calls Constructor Implicitly / Automatically
print("Content of s =",s.__dict__)
s1 = Student()
print("Content of s1 =",s1.__dict__)