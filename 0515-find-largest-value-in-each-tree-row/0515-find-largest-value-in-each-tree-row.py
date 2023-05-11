# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        from collections import deque
        q=deque()
        ans=[]
        q.append(root)
        while len(q)>0:
            size=len(q)
            maxx=float('-inf')
            for i in range(size):
                node=q.popleft()
                maxx=max(maxx,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(maxx)
        return ans    
                
        