# 19. Remove Nth Node From End of List

def func(head,n):
    length = 0
    temp = head
    while temp != None:
        length += 1
        temp = temp.next
    if length == n:
        return head.next
    pos_to_stop = length - n
    count = 1
    temp = head
    while count < pos_to_stop:
        temp = temp.next
        count += 1
    temp.next = temp.next.next
    return head


def func(head,n):
    fast = head
    slow = head
    for _ in range(n):
        fast = fast.next
    if fast == None:
        return head.next
    while fast.next != None:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head