"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        from collections import deque
        if node==None:
            return None
        q=deque()
        d={}
        newnode=Node(node.val)
        d[node]=newnode
        q.append(node)
        while len(q)>0:
            tnode=q.popleft()
            for i in tnode.neighbors:
                if i in d:
                    d[tnode].neighbors.append(d[i])
                else:
                    newnode=Node(i.val)
                    d[i]=newnode
                    d[tnode].neighbors.append(d[i])
                    q.append(i)
                    
        return d[node]
    
        