# 206. Reverse Linked List


# Brute  TC--> O(2N)   SC--> O(N)
def reverseList(head):
    temp = head
    lst = []
    while temp != None:
        lst.append(temp.val)
        temp = temp.next
    temp = head
    while temp != None:
        temp.val = lst.pop()
        temp = temp.next
    return head


# Optimal  TC-->  O(N)   SC--> O(1)
def reverseList(head):
    prev = None
    temp = head
    while temp != None:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev