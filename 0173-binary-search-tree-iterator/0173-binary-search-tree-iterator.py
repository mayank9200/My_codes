# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    #https://www.youtube.com/watch?v=D2jMcmxU4bs
    #it is basically inorder traversal of a tree in iterative way using stack
    from collections import deque
    def insertstack(self,root): #function to go to extream left
        while root!=None:
            self.s.appendleft(root)
            root=root.left
            
    def __init__(self, root: Optional[TreeNode]):
        self.s=deque()
        self.insertstack(root)
        
        

    def next(self) -> int:
        val=self.s.popleft() #print the top of stack and push its right to to stack to go till extream left
        self.insertstack(val.right)
        return val.val
        

    def hasNext(self) -> bool: #if stack is empty or nor
        return len(self.s)

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()