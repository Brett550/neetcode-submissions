# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # answer = []
        ordered = self.inOrder(root, [])
        # print(ordered)
        return ordered[k-1]

    def inOrder(self, node, answer):
        if node:
            # go left
            self.inOrder(node.left, answer)

            #process
            answer.append(node.val)

            #go right
            self.inOrder(node.right, answer)
        return answer