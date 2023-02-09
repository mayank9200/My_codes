# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    #simple level order traversal
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
                    res=res+'#,' #if none so add # and a comma,comma because it acts as a separator while deserializing
                    break
                else:
                    res=res+str(node.val)+',' #adding value and comma,comma because it acts as a separator while deserializing
                q.append(node.left)
                q.append(node.right)
        return res        
                    
            
                
                
        
        
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        #traverse the string and make connections
        data=data.split(',') #split data in a char array to know actual numbers(cases like -1,-2001)
        if data[0]=='#': #if first is only none
            return None
        from collections import deque
        q=deque()
        k=0
        root=TreeNode(data[k]) #make actual nodes now
        k+=1
        q.append(root)
        while len(q)>0:
            size=len(q)
            for i in range(size):
                node=q.popleft()
                if data[k]!='#': #if some value is there then make connections
                    node.left=TreeNode(int(data[k]))
                    q.append(node.left)
                
                    
                k+=1
                if data[k]!='#': #if some value is there then make connections
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