# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        if root==None:
            return 0
        q=deque()
        q.append([root,False])
        summ=0
        while len(q)>0:
            size=len(q)
            for i in range(size):
                node,isleft=q.popleft()
                if node.left==None and node.right==None and isleft==True:
                    summ+=node.val
                if node.left:
                    q.append([node.left,True])
                if node.right:
                    q.append([node.right,False])
        return summ            
                    
        