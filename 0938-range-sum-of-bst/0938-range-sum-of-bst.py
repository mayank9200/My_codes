# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #simple just make cases
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root==None:
            return 0
        if root.val>=low and root.val<=high:
            return root.val+self.rangeSumBST(root.left,low,high)+self.rangeSumBST(root.right,low,high)
        if root.val>low:
            return self.rangeSumBST(root.left,low,high)
        else:
            return self.rangeSumBST(root.right,low,high)
        