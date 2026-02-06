# Program for Demonstrating local and Global Variables

def learAI():
    sub1 = "AI" # Local Var
    print("To develop '{}' Application we use '{}' Prog Lang".format(sub1,lang))

def learML():
    sub2 = "ML" # Local Var
    print("To develop '{}' Application we use '{}' Prog Lang".format(sub2,lang))

def learDL():
    sub3 = "DL" # Local Var
    print("To develop '{}' Application we use '{}' Prog Lang".format(sub3,lang))

lang = "PYTHON" # Global Var
learAI()
learML()
learDL()