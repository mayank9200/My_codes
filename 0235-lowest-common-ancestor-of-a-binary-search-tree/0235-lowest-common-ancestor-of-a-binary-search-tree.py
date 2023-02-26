# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #very simple 
        while root!=None:
            if p.val>root.val and q.val>root.val: #ancestor can be at right
                root=root.right
            elif p.val<root.val and q.val<root.val: #ancestor can be at left
                root=root.left
            else: 
                return root #got the ancestor
        return None    
        