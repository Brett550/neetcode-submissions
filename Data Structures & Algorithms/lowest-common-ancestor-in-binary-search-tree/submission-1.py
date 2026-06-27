# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        smallest = min(p.val, q.val)
        biggest = max(p.val, q.val)
        if root.val > biggest:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < smallest:
            return self.lowestCommonAncestor(root.right, p, q)
        return root