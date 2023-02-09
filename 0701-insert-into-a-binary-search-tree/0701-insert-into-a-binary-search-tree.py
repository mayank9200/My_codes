# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr=root
        prev=None
        while curr!=None:
            prev=curr
            if val<curr.val:
                curr=curr.left
            else:
                curr=curr.right
        if prev==None:
            return TreeNode(val)
        else:
            if val<prev.val:
                prev.left=TreeNode(val)
            else:
                prev.right=TreeNode(val)
        return root        