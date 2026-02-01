# Define a function for cal area of Rectangle

def area_rect(l,w):
    area = l * w
    print("Area of Rectangle is = {}".format(area))
    print("-"*35)

print("-"*35)
length = float(input("Enter Legnth of Rectangle: "))
width = float(input("Enter Width of Rectangle: "))

area_rect(length,width)