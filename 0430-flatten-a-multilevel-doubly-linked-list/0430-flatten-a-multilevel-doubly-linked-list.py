"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    from collections import deque
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        if curr==None:
            return head
        while curr!=None:
            if curr.child!=None:
                nhead=self.flatten(curr.child)
                t1=nhead
                while nhead.next!=None:
                    nhead=nhead.next
                nhead.next=curr.next
                if curr.next:
                    curr.next.prev=nhead
                curr.next=t1
                t1.prev=curr
                curr.child=None
            curr=curr.next
        return head    
            
            
        
       
        