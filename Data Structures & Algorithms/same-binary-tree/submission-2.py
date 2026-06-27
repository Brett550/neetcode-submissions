# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and not q) or (not p and q):
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False
        return self.isSameTreeRec(p.left, q.left) and self.isSameTreeRec(p.right, q.right)
        
        # return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    def isSameTreeRec(self, p, q):
        if (p and not q) or (not p and q):
            return False
        elif not p and not q:
            return True
        if p.val != q.val:
            return False
        # elif p.val == q.val:
        #     return True
        return self.isSameTreeRec(p.left, q.left) and self.isSameTreeRec(p.right, q.right)