# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.preindex=0
    def tree(self,preorder,inorder,s,e,d):
        if s>e:
            return None
        root=TreeNode(preorder[self.preindex])
        self.preindex+=1
        inindex=d[root.val]
        root.left=self.tree(preorder,inorder,s,inindex-1,d)
        root.right=self.tree(preorder,inorder,inindex+1,e,d)
        return root
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d={}
        for i in range(len(inorder)):
            d[inorder[i]]=i
        root=self.tree(preorder,inorder,0,len(inorder)-1,d)    
        return root
        