# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,k,ans):
        if root:
            self.inorder(root.left,k,ans)
            k[0]-=1
            if k[0]==0:
                ans[0]=root.val
                return
            self.inorder(root.right,k,ans)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[0]
        k=[k]
        self.inorder(root,k,ans)
        return ans[0]