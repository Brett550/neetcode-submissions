# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        maxi = float('inf')
        mini = float('-inf')
        # if root == None:
        #     return True
        # if root.left and root.left.val >= root.val:
        #     return False
        # if root.right and root.right.val <= root.val:
        #     return False
        # if root.right == None and root.left == None:
        #     return True
        return self.validBSTRecur(root, mini, maxi)
    
    def validBSTRecur(self, root, mini, maxi):
        if root == None:
            return True
        if root.right == None and root.left == None:
            return True
        if root.left and (root.left.val >= root.val or root.left.val >= maxi or root.left.val <= mini):
            return False
        if root.right and (root.right.val <= root.val or root.right.val <= mini or root.right.val >= maxi):
            return False
        
        return self.validBSTRecur(root.left, mini, root.val) and self.validBSTRecur(root.right, root.val, maxi)
