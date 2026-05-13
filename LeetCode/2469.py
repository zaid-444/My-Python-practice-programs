# 2469. Convert the Temperature

def convertTem(celsius):
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32
    l = []
    l.append(kelvin)
    l.append(fahrenheit)
    return l

cel = float(input("Enter Celsius to Convert: "))
print("-"*50)
print("Temprature {} in Kelvin and Fahrenheit = {}".format(cel,convertTem(cel)))
print("-"*50)