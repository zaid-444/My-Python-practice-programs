# Program for Demonstrating Keyword Arguments

def disp(A,B,C,D):
    print("\t{}\t{}\t{}\t{}".format(A,B,C,D))

print("-"*50)
print("\tA\tB\tC\tD")
print("-"*50)
disp(10,20,30,40) # Possitional arguments
disp(B=20,D=40,C=30,A=10) # Keyword arguments
disp(10,20,D=40,C=30) # Possitional and Keyword arguments
print("-"*50)