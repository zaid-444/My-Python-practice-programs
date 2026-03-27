# 19. Write a Python program to get the difference between the two lists.

print("Enter List1 Elements")
l1 = [ val for val in input().split() ]
print("Enter List2 Elements")
l2 = [ val for val in input().split() ]

dl1 = [ val for val in l1 if val not in l2 ]
dl2 = [ val for val in l2 if val not in l1 ]

print("Difference in l1=",dl1)
print("Difference in l2=",dl2)
