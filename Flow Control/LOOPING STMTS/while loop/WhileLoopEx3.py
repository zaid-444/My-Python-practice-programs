# program to generate all even numbers within n

n = int(input("Enter How many Even numbers u want to generate within range: "))

# if n <= 0:
#     print("{} is Invalid input".format(n))
# else:
#     i = 2
#     while i <= n:
#         if i%2 == 0:
#             print(i)
#         i += 1

if n <= 0:
    print("{} Invalid input".format(n))
else:
    i = 2
    while i <= n:
        print(i)
        i += 2