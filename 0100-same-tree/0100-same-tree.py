# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    #https://www.youtube.com/watch?v=BhuvF_-PWS0
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None or q==None: #base condition
            if p==q: #if both are none then it is identical
                return True
            else:
                return False #if one is none and other is not then not identical
        return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)     #just a simple preorder traversal
        
        