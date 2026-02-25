
def gencourses():
    yield "PYTHON"
    yield "JAVA"
    yield "C"
    yield "C++"
    yield "HTML"
    yield "JavaScript"

crs = gencourses()
print(next(crs))
print(next(crs))
print(next(crs))
print(next(crs))
