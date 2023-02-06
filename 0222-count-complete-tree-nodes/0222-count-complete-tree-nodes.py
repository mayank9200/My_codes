# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        left=0
        right=0
        curr=root
        while curr!=None:
            left+=1
            curr=curr.left
        curr=root
        while curr!=None:
            right+=1
            curr=curr.right
        if left==right:
            return pow(2,left)-1
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
        
        