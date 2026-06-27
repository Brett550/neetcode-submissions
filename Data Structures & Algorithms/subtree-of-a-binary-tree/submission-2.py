# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if (root and not subRoot) or (not root and subRoot):
            return False
        if root.val == subRoot.val:
            result = self.isSameTreeRec(root, subRoot)
            if result:
                return result
            else:
                return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

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