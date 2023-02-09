# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        from collections import deque
        q=deque()
        q.append(root)
        res=''
        while len(q)>0:
            size=len(q)
            for i in range(size):
                node=q.popleft()
                if node==None:
                    res=res+'#,'
                    break
                else:
                    res=res+str(node.val)+','
                q.append(node.left)
                q.append(node.right)
        return res        
                    
            
                
                
        
        
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        data=data.split(',')
        if data[0]=='#':
            return None
        from collections import deque
        q=deque()
        k=0
        root=TreeNode(data[k])
        k+=1
        q.append(root)
        while len(q)>0:
            size=len(q)
            for i in range(size):
                node=q.popleft()
                if data[k]!='#':
                    node.left=TreeNode(int(data[k]))
                    q.append(node.left)
                
                    
                k+=1
                if data[k]!='#':
                    node.right=TreeNode(int(data[k]))
                    q.append(node.right)
                  
                k+=1    
        return root
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))