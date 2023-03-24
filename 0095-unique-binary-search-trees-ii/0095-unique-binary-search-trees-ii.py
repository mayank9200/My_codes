# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        #https://www.youtube.com/watch?v=qOItdXuTZGo
        #somewhat similar to create tree from preorder and inorder
        ans=[]
        start=1 #start from 1
        end=n #end at n
        def helper(n,start,end):
            if start>end:  #if they cross each other
                return [None] #only None will be in list
            ans=[]
            for k in range(start,end+1): #make everyone root
                left=helper(n,start,k-1) #gives left root list
                right=helper(n,k+1,end) #gives right root list
                #make every combination of left with right(left=m,right=n, so trees with this root will be left*right)
                for i in left:
                    for j in right:
                        root=TreeNode(k) #make k root
                        root.left=i #do left connection
                        root.right=j #do right connection
                        ans.append(root) #append one ans
            return ans  #return that ans
        return helper(n,start,end)
        