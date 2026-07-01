# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = self.smallCur(root, [])

        return arr[k-1]

    def smallCur(self, root, ordered):
        if root:
            self.smallCur(root.left, ordered)

            ordered.append(root.val)

            self.smallCur(root.right, ordered)

        return ordered

