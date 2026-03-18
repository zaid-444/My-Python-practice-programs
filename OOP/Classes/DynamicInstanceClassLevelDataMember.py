# Program for Demonstrating Instance Data Members and Class Level Data Members

class Student:
    crs = "PYTHON"  # Class LVL Data Member
    city = "PUNE"

print("-"*50)
s1 = Student()
s1.sno = int(input("Enter First Student Number: "))
s1.sname = input("Enter First Student Name: ")
s1.marks = float(input("Enter First Student Marks: "))



s2 = Student()
s2.sno = int(input("Enter Second Student Number: "))
s2.sname = input("Enter Second Student Name: ")
s2.marks = float(input("Enter Second Student Marks: "))

print("-"*50)

print("\tFirst Student Details")
print("Student Number:",s1.sno)
print("Student Name:",s1.sname)
print("Student Marks:",s1.marks)
print("Student Course:",s1.crs)
print("Student City:",s1.city)
print("-"*50)
print("\tSecond Student Details")
print("Student Number:",s2.sno)
print("Student Name:",s2.sname)
print("Student Marks:",s2.marks)
print("Student Course:",s2.crs)
print("Student City:",s2.city)

print("-"*50)