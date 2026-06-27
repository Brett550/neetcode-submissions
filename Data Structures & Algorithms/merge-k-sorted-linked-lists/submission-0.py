# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        start = self.mergeTwoLists(lists[0], lists[1])
        for list in lists[2:]:
            start = self.mergeTwoLists(start, list)
        return start

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next
        
        # allLists = []
        # for list in lists:
        #     cur = list
        #     while cur != None:
        #         allLists.append(cur.val)
        #         cur = cur.next
        # allLists.sort()
        # print(allLists)

        # head = ListNode()
        # ogHead = head
        # for value in allLists:
        #     head.val = value
        #     head.next = ListNode()
        #     prev = head
        #     head = head.next
        # return ogHead
        