# Program for demonstrating Class Level Data Members

class Student:
    course = "PYTHON" # Class LVL Data Member

s1 = Student()
s2 = Student()

print("content of s1 =",s1.__dict__) # {}
print("content of s2 =",s2.__dict__)

# Course is not a part of s1 and s2

# Accessing CLS LVL data member using Class Name
print("Content of s1-Class Level data Member =",Student.course)
print("Content of s2-Class Level data Member =",Student.course)

print("-------------------------OR-------------------------")

# Accessing CLS LVL data member using Object Name
print("Content of s1-Class Level data Member =",s1.course)
print("Content of s2-Class Level data Member =",s1.course)