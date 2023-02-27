# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        q=deque()
        q.append(root)
        maxx=float('-inf')
        index=1
        level=1
        while len(q)>0:
            size=len(q)
            summ=0
            for i in range(size):
                node=q.popleft()
                summ=summ+node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if summ>maxx:
                maxx=summ
                index=level
            level+=1
        return index     
                    
                
        