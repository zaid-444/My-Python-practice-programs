# 412. Fizz Buzz

def fizzBuzz(n):
    lst = []
    for i in range(1,n+1):
        if i%3 == 0 and i%5 == 0:
            lst.append("FizzBuzz")
        elif i%3 == 0:
            lst.append("Fizz")
        elif i%5 == 0:
            lst.append("Buzz")
        else:
            lst.append(str(i))
    return lst


n = int(input("Enter value of N: "))
print("~"*40)
print(f"Output: {fizzBuzz(n)}")
print("~"*40)