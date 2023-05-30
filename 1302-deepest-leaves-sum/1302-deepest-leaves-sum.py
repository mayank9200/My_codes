# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if root==None:
            return 0
        return 1+max(self.height(root.left),self.height(root.right))
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        h=self.height(root)
        from collections import deque
        q=deque()
        q.append(root)
        level=0
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
            level+=1
            if level==h:
                return summ
        return 0   
        