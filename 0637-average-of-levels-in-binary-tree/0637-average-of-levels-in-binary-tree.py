# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root==None:
            return 0
        from collections import deque
        q=deque()
        ans=[]
        q.append(root)
        while len(q)>0:
            size=len(q)
            summ=0
            for i in range(size):
                node=q.popleft()
                summ+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(summ/size)
        return ans     
        