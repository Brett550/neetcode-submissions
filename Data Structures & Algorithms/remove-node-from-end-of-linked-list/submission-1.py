# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length of list
        length = 0
        cur = head
        while cur != None:
            cur = cur.next
            length += 1

        # remove the node
        cur = head
        index = 0
        while index < (length - n - 1):
            cur = cur.next
            index += 1
        
        
        # now we at the node right before the one to remove
        if (length - n - 1) < 0: #special case: removing the head
            head = cur.next
        else:
            cur.next = cur.next.next if cur.next.next else None
        return head

        
        

