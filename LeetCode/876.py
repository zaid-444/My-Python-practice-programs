# 876. Middle of the Linked List


# Brute TC--> O(N+n/2)     SC--> O(1)
def middleNode(head):
    temp = head
    c = 0
    while temp != None:
        c += 1
        temp = temp.next
    temp = head
    for _ in range(c//2):
        temp = temp.next
    return temp


# Optimal  TC--> O(N/2)     SC--> O(1)
def middleNode(head):
    fast = head
    slow = head
    while fast != None and fast.next != None:
        fast = fast.next
        fast = fast.next
        slow = slow.next
    return slow