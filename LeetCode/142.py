# 142. Linked List Cycle ||

def detectCycle(head):
    temp = head
    s = set()
    while temp != None:
        if temp in s:
            return temp
        s.add(temp)
        temp = temp.next
    return None


def detectCycle(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None