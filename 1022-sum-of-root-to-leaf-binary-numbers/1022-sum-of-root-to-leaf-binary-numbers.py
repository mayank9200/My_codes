# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        q=deque()
        q.append([root,root.val])
        summ=0
        while len(q)>0:
            size=len(q)
            for i in range(size):
                node,val=q.popleft()
                if node.left:
                    q.append([node.left,val*2+node.left.val])
                if node.right:
                    q.append([node.right,val*2+node.right.val])
                if node.left==None and node.right==None:
                    summ=summ+val 
        return summ