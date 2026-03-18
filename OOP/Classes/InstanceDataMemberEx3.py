# Program for Demonstrating Instance Data Members

class Student:pass

print("-"*50)
s1 = Student()
s2 = Student()

print("Id of s2 =",id(s2))
print("Id of s1 =",id(s1))
print("-"*50)


print("Initial Content of s1={} and No. of Values={}".format(s1.__dict__,len(s1.__dict__)))
print("Initial Content of s2={} and No. of Values={}".format(s2.__dict__,len(s2.__dict__)))
print("-"*50)


s1.sno = 101
s1.sname = "Zaid"
s1.marks = 98.30

s2.sno = 102
s2.sname = "Virat"
s2.marks = 84.22
s2.collage = "MVP"

print("First Student Details")

for k,v in s1.__dict__.items():
    print("{} = {}".format(k,v))

print("-"*50)

print("Second Student Details")

for k,v in s2.__dict__.items():
    print("{} = {}".format(k,v))

print("-"*50)