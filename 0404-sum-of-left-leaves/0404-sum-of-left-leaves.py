# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #level order traversal
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        if root==None:
            return 0
        q=deque()
        q.append([root,False]) #[root,isleft] isleft will. be true only when it is left node
        summ=0
        while len(q)>0:
            size=len(q)
            for i in range(size):
                node,isleft=q.popleft()
                if node.left==None and node.right==None and isleft==True:#just one condition if it is left node and both of its child are None then only sum
                    summ+=node.val
                if node.left:
                    q.append([node.left,True]) #when insert left mark isleft as True
                if node.right:
                    q.append([node.right,False]) #when insert right mark isleft as False
        return summ            
                    
        