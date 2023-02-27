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
        summ=summ+root.val #summ till now, basically prefix sum
        if summ-target in d: #got one ans
            count[0]+=d[summ-target] #how many times we got subarrays earlier, sabke sath combinations banenge
        d[summ]=d.get(summ,0)+1 #increment the prefix sum
        self.solve(root.left,d,summ,target,count)
        self.solve(root.right,d,summ,target,count)
        d[summ]-=1 #backtrack, decrease the prefix sum
        if d[summ]==0: 
            d.pop(summ)
            
            
            
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        #https://www.youtube.com/watch?v=yyZA4v0x16w
        #similar to subarray sum of size k problem
        d={}
        d[0]=1 # for the cases of prefix sum as 0, you can also add another if condition instead of this
        count=[0]
        self.solve(root,d,0,targetSum,count)
        return count[0]
        