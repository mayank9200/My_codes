# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #https://www.youtube.com/watch?v=bTA3OLAeTi4
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        #keep it simple
        if root==None: #if root is None
            return None
        if root.val>=low and root.val<=high: 
            root.left=self.trimBST(root.left,low,high)
            root.right=self.trimBST(root.right,low,high)
        elif root.val>high: # search ans on left
            return self.trimBST(root.left,low,high)
        elif root.val<low: #search ans on right
            return self.trimBST(root.right,low,high)
        return root #root is the ans