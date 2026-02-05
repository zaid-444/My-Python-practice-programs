# Program for Demonstrating Variable Length Arguments (OR) Parameters

def dispvals(*a): # here *a is called Variable Length Param and whose type is tuple
    print("-"*50)
    for v in a:
        print(v,end=" ")
    print()

dispvals(10,20,30,40,50) # Function Call-1 with 5 Pos Args
dispvals(10,20,30,40) # Function Call-2 with 4 Pos Args
dispvals(10,20,30) # Function Call-3 with 3 Pos Args
dispvals(10,20) # Function Call-4 with 2 Pos Args
dispvals(10) # Function Call-5 with 1 Pos Args
dispvals() # Function Call-6 with 0 Pos Args