# Program for Class and objects without using Constructor

class Student: 
    def sudval(self):
        self.sno = 444
        self.name = "Zaid"

s = Student() # Object Creation
print("Content =",s.__dict__)
# Placing Data Members inside of object's using Instance Method
s.sudval() # For setting the vals in obj we are calling a method Explicitly
print("Content =",s.__dict__)
