# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2

        if list1 == None:
            return cur2
        elif list2 == None:
            return cur1

        newList = None

        curMin = min(cur1.val,cur2.val)
        newList = None
        if curMin == cur1.val:
            newList = cur1
            cur1 = cur1.next
        elif curMin == cur2.val:
            newList = cur2
            cur2 = cur2.next

        newHead = newList #keep ponter to head of new list

        #main assembly
        while cur1 != None and cur2 != None:
            curMin = min(cur1.val,cur2.val)
            if curMin == cur1.val:
                newList.next = cur1
                cur1 = cur1.next
            elif curMin == cur2.val:
                newList.next = cur2
                cur2 = cur2.next
            newList = newList.next
        #finish adding any list (one longer than other)
        if cur1 != None:
            newList.next = cur1
        elif cur2 != None:
            newList.next = cur2

        return newHead



        