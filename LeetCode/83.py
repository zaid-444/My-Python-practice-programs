# 83. Remove Duplicates from Sorted List

def deleteDupli(head):
    if head == None or head.next == None:
        return head
    curr = head
    while curr != None and curr.next != None:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head