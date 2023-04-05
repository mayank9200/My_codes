# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,fval,ans):
        if root!=None:
            self.inorder(root.left,fval,ans)
            ans.add(root.val)
            self.inorder(root.right,fval,ans)
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        fval=[-1]
        ans=set()
        self.inorder(root,fval,ans)
        val=min(ans)
        ans.remove(val)
        if len(ans)==0:
            return -1
        
        return min(ans)
        