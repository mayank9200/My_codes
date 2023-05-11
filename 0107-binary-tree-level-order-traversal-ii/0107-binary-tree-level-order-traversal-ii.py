# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        from collections import deque
        q=deque()
        q.append(root)
        ans=[]
        while len(q)>0:
            size=len(q)
            tans=[]
            for i in range(size):
                node=q.popleft()
                tans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(tans) 
        return ans[::-1]    
                    
        