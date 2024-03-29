# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #https://www.youtube.com/watch?v=R9qiY7OK9JQ
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #the key is ki har node ko number dedo just like in heap and in level order traversal last-start+1 ka max is the ans, left=2*i+1,right=2*i+2
        from collections import deque
        q=deque() 
        q.append([root,0]) #[root,position]
        maxx=0
        while len(q)>0:
            size=len(q)
            for i in range(size):
                node,j=q.popleft()
                if i==0:
                    c1=j
                if i==size-1:
                    c2=j
                if node.left:
                    q.append([node.left,2*j+1])
                if node.right:
                    q.append([node.right,2*j+2])    
            maxx=max(maxx,c2-c1+1)
        return maxx    
                
                
                
            
        