# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None:
            return None
        if root==p or root==q:
            return root
        lca1=self.lowestCommonAncestor(root.left,p,q)
        lca2=self.lowestCommonAncestor(root.right,p,q)
        if lca1!=None and lca2!=None:
            return root
        if lca1==None:
            return lca2
        else:
            return lca1
            
        