# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []

        q = deque()
        q.append(root)

        while q:
            level = [] #assemble list for current level
            length = len(q)
            for i in range(length):
                node = q.popleft() #get current node
                if node:
                    level.append(node.val) #add node to list
                    #add children to queue
                    q.append(node.left) 
                    q.append(node.right)
            if level: 
                answer.append(level) #append this list if it has items

        return answer