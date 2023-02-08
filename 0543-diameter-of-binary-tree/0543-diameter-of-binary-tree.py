# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkdiameter(self,root,maxx): #just return diameter when it passes through root
        if root==None:
            return 0
        lh=self.checkdiameter(root.left,maxx)
        rh=self.checkdiameter(root.right,maxx)
        maxx[0]=max([maxx[0],lh+rh+1])
        return 1+max(lh,rh)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxx=[0]
        self.checkdiameter(root,maxx)
        return maxx[0]-1 #edges return karni
        
        