# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #first thought: convert to array, use 2 pointers to do it, convert back to linkedlist
            #O(N) runtime, O(N) space complexity

        #create the array
        answer = []
        arr = []
        cur = head
        while cur != None:
            arr.append(cur.val)
            cur = cur.next

        left = 0
        right = len(arr)-1

        while left < right:
            answer.append(arr[left])
            answer.append(arr[right])
            left += 1
            right -= 1
        if arr[left] not in answer: #check for when list length is odd
            answer.append(arr[left])

        # print("answer is", answer)

        # turn back into linkedlist
        head.val = answer[0]
        ogHead = head

        # print(ogHead.val)

        for value in answer[1:]:
            head.next = ListNode()
            head = head.next
            head.val = value
            print(head.val)
        head = ogHead

            #how to reduce space complexity? Do it in place
        # how do it in place with SINGLY linked list???
            #maybe put all things in a stack... still not O(1) space