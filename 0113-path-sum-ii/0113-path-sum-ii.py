# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root==None:
            return []
        from collections import deque
        q=deque()
        q.append([root,root.val,[root.val]])
        ans=[]
        while len(q)>0:
            size=len(q)
            for i in range(size):
                node,summ,l=q.popleft()
                if node.left:
                    q.append([node.left,summ+node.left.val,l+[node.left.val]])
                if node.right:
                    q.append([node.right,summ+node.right.val,l+[node.right.val]])    
                if node.left==None and node.right==None and summ==targetSum:
                    ans.append(l)
        return ans            