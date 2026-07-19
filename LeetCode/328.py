# 328. Odd Even Linked List


# Brute  TC--> O(N)     SC--> O(N)
def func(head):
    if head is None or head.next is None:
        return head
    l = []
    temp = head
    while temp:
        l.append(temp.val)
        if temp.next:
            temp = temp.next.next
        else:
            temp = None
    temp = head.next
    while temp:
        l.append(temp.val)
        if temp.next:
            temp = temp.next.next
        else:
            temp = None
    temp = head
    i = 0
    while temp:
        temp.val = l[i]
        i += 1
        temp = temp.next
    return head