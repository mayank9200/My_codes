# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        ans=[]
        start=1
        end=n
        def helper(n,start,end):
            if start>end:
                return [None]
            ans=[]
            for k in range(start,end+1):
                left=helper(n,start,k-1)
                right=helper(n,k+1,end)
                for i in left:
                    for j in right:
                        root=TreeNode(k)
                        root.left=i
                        root.right=j
                        ans.append(root)
            return ans  
        return helper(n,start,end)
        