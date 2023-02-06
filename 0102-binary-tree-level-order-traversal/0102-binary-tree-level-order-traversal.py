# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if root==None:
            return None
        q=deque()
        q.append(root)
        ans=[]
        while len(q)>0:
            size=len(q)
            t_ans=[]
            for i in range(size):
                node=q.popleft()
                t_ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(t_ans)
        #print(ans)
        return ans    