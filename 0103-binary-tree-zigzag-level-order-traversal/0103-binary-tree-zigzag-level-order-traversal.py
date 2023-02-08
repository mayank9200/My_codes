# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if root==None:
            return None
        q=deque()
        s=deque()
        res=[]
        flag=True
        q.append(root)
        while len(q)>0:
            size=len(q)
            ans=[]
            for i in range(size):
                node=q.popleft()
                if flag:
                    ans.append(node.val)
                else:
                    s.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            while len(s)>0:
                ans.append(s.popleft())
            res.append(ans)
            if flag:
                flag=False
            else:
                flag=True
        return res     