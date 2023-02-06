# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,flag): #simple height calculate function
        if root==None:
            return 0
        lh=self.solve(root.left,flag)
        rh=self.solve(root.right,flag)
        if abs(lh-rh)>1: #global variable ek baar bhi height me 1 se jyada ka diff
            flag[0]=False
        return 1+max(lh,rh)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        flag=[True]
        self.solve(root,flag)
        return flag[0]
        