# Define a function for cal area of Rectangle

def area_rect(l,w):
    area = l * w
    return area


print("-"*40)
length = float(input("Enter Legnth of Rectangle: "))
width = float(input("Enter Width of Rectangle: "))

res = area_rect(length,width)
print("Area of Rectangle is = {}".format(res))
print("-"*40)