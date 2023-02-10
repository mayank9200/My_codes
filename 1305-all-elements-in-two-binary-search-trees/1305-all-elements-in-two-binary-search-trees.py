# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root,ans):
        if root:
            self.inorder(root.left,ans)
            ans.append(root.val)
            self.inorder(root.right,ans)
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1=[]
        l2=[]
        self.inorder(root1,l1)
        self.inorder(root2,l2)
        m=len(l1)
        n=len(l2)
        i=0
        j=0
        res=[]
        while i<m and j<n:
            if l1[i]<=l2[j]:
                res.append(l1[i])
                i+=1
            else:
                res.append(l2[j])
                j+=1
        while i<m:
            res.append(l1[i])
            i+=1
        while j<n:
            res.append(l2[j])
            j+=1
        return res    
        
        