# Program for Demonstrating Instance Data Members and Class Level Data Members

class Student:
    crs = "PYTHON"  # Class LVL Data Member
    city = "PUNE"

print("-"*50)
s1 = Student()
s1.sno = 101
s1.sname = "Zaid"
s1.marks = 72.35
print("Id of s1 =",id(s1))


s2 = Student()
s2.sno = 102
s2.sname = "Rohit"
s2.marks = 83.33
print("Id of s2 =",id(s2))
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