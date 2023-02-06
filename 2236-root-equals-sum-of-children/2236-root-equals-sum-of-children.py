# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
        if root.left==None and root.right==None:
            return True
        summ=0
        if root.left:
            summ=summ+root.left.val
        if root.right:
            summ=summ+root.right.val
        return summ==root.val and self.checkTree(root.left) and self.checkTree(root.right)    
        