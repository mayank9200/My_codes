# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree(self,inorder,postorder,s,e,d,postindex):
        if s>e:
            return None
        root=TreeNode(postorder[postindex[0]])
        postindex[0]-=1
        inindex=d[root.val]
        root.right=self.tree(inorder,postorder,inindex+1,e,d,postindex)
        root.left=self.tree(inorder,postorder,s,inindex-1,d,postindex)
        return root
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        d={}
        for i in range(len(inorder)):
            d[inorder[i]]=i
        postindex=[len(postorder)-1]  
        root=self.tree(inorder,postorder,0,len(postorder)-1,d,postindex)    
        return root
        