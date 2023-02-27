# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def making_parent(self,root,prev,parent,visited):
        if root:
            parent[root]=prev
            visited[root]=False
            prev=root
            self.making_parent(root.left,prev,parent,visited)
            self.making_parent(root.right,prev,parent,visited)
            
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if root==None:
            return []
        if k==0:
            return [target.val]
        from collections import deque
        parent={}
        visited={}
        prev=None
        self.making_parent(root,prev,parent,visited)
        curr=target
        q=deque()
        q.append(target)
        visited[target]=True
        while len(q)>0:
            size=len(q)
            for i in range(size):
                node=q.popleft()
                visited[node]=True
                if node.left and visited[node.left]==False:
                    q.append(node.left)
                if node.right and visited[node.right]==False:
                    q.append(node.right)
                if parent[node] and visited[parent[node]]==False:
                    q.append(parent[node])
            k-=1
            if k==0:
                break
        ans=[]
        while len(q)>0:
            ans.append(q.popleft().val)
        return ans             
        
        