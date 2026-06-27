# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.depth(root.left, 1), self.depth(root.right, 1))
    def depth(self, node, length):
        if node is None:
            return length
        length +=1
        return max(self.depth(node.left, length),self.depth(node.right, length))
