def lower(z):
    def lw():
        t,u = z()
        l = t.lower()
        return t,u,l
    return lw

def upper(x):
    def up():
        u = x()
        return u,u.upper()
    return up


@lower
@upper
def gettxt():
    return input("Enter line of text: ")

x,y,z = gettxt()
print("Line of Text: [{}]".format(x))
print("Upper Line  : [{}]".format(y))
print("Lower Line  : [{}]".format(z))