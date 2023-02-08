# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #this is basically traversing path solution
    def findpath(self,root,ans,res,val):
        if root==None:
            return 
        if root.val==val:
            ans.append(root)
            res.append(ans)
            return 
        if root.left:
            self.findpath(root.left,ans+[root],res,val)
        if root.right:
            self.findpath(root.right,ans+[root],res,val)
        
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1=[]
        path2=[]
        ans=[]
        self.findpath(root,ans,path1,p.val)
        self.findpath(root,ans,path2,q.val)
        path1=path1[0]
        path2=path2[0]
        if path1==[] or path2==[]:
            return None
        m=len(path1)
        n=len(path2)
        i=0
        j=0
        while i<m and j<n:
            if path1[i].val!=path2[j].val:
                break
            i+=1
            j+=1
        return path1[i-1]