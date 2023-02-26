# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        q=deque()
        q.append(root)
        ans=root
        while len(q)>0:
            size=len(q)
            for i in range(size):
                node=q.popleft()
                if i==0:
                    ans=node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans.val            
        