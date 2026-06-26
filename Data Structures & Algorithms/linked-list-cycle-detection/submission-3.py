# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        elif head.next is None:
            return False
        elif head.next == head:
            return True
        
        cur1 = head
        cur2 = head
        start = True


        while cur1 != None and cur2 != None:
            if cur1 == cur2 and not start:
                return True
            try:
                cur1=cur1.next
                cur2=cur2.next.next
            except:
                break
            start = False
        return False