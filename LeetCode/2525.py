# 2525. Categorize Box According to Criteria

def categorizeBox(length,width,height,mass):
    bulky = False
    heavy = False
    if length >= 10**4 or width >= 10**4 or height >= 10**4 or (length*width*height) >= 10**9:
        bulky = True
    if mass >= 100:
        heavy = True
    if heavy and bulky:
        return "Both"
    elif not heavy and not bulky:
        return "Neither"
    elif bulky and not heavy:
        return "Bulky"
    else:
        return "Heavy"
    


length = int(input("Enter lenght of the box: "))
width = int(input("Enter width of the box: "))
height = int(input("Enter height of the box: "))
mass = int(input("Enter mass of the box: "))
res = categorizeBox(length,width,height,mass)

print("~"*30)
print("Output:",res)
print("~"*30)