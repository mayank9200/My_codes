# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root):
        if root==None:
            return 0
        lh=self.solve(root.left)
        rh=self.solve(root.right)
        if lh==-1:
            return -1
        if rh==-1:
            return -1
        if abs(lh-rh)<=1:
            return max(lh,rh)+1
        else:
            return -1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans=self.solve(root)
        if ans==-1:
            return False
        return True
        