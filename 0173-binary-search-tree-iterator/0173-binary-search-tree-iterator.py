# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    from collections import deque
    def insertstack(self,root):
        while root!=None:
            self.s.appendleft(root)
            root=root.left
            
    def __init__(self, root: Optional[TreeNode]):
        self.s=deque()
        self.insertstack(root)
        
        

    def next(self) -> int:
        val=self.s.popleft()
        self.insertstack(val.right)
        return val.val
        

    def hasNext(self) -> bool:
        return len(self.s)

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()