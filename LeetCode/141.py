# 141. Linked List Cycle


# Brute  TC--> O(N)   SC--> O(N)
def hasCycle(head):
    s = set()
    temp = head
    while temp != None:
        if temp in s:
            return True
        s.add(temp)
        temp = temp.next
    return False


# Optimal   TC--> O(N)  SC--> O(1)
def hasCycle(head):
    fast = head
    slow = head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False