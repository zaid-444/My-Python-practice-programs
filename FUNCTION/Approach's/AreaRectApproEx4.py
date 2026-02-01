# Define a function for cal area of Rectangle

def area_rect():
    print("-"*40)
    length = float(input("Enter Length of Rectangle: "))
    width = float(input("Enter Width of Rectangle: "))
    area = length * width
    return area

res = area_rect()
print("Area of Rectangle is = {}".format(res))
print("-"*40)