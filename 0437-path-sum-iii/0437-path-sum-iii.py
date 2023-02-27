# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,root,d,summ,target,count):
        if root==None:
            return 
        summ=summ+root.val
        if summ-target in d:
            count[0]+=d[summ-target]
        d[summ]=d.get(summ,0)+1
        self.solve(root.left,d,summ,target,count)
        self.solve(root.right,d,summ,target,count)
        d[summ]-=1
        if d[summ]==0:
            d.pop(summ)
            
            
            
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        d={}
        d[0]=1
        count=[0]
        self.solve(root,d,0,targetSum,count)
        return count[0]
        