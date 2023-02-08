# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':# 4 cases
        if root==None: #if both of them are neither in left or in right
            return None
        if root==p or root==q:
            return root
        lca1=self.lowestCommonAncestor(root.left,p,q) #simply gives lca from left if exist
        lca2=self.lowestCommonAncestor(root.right,p,q) #simply gives lca from right if exist
        if lca1!=None and lca2!=None: #if both of them are either in left subtree or right subtree
            return root
        if lca1==None: #if both are in left only
            return lca2
        else: #if both are in right only
            return lca1
            
        