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
        if curr==None: #base condition since using recursion
            return head
        while curr!=None: #traverse till end
            if curr.child!=None: #if child does not exist
                nhead=self.flatten(curr.child) #magically the below list is flattened
                t1=nhead #keep its head safe
                while nhead.next!=None: #find the last node of the flattened list
                    nhead=nhead.next
                nhead.next=curr.next # do the linking of last node of flattened to orignal
                if curr.next: 
                    curr.next.prev=nhead #linking of last node of flattend to orignal
                curr.next=t1 #linking of first node of flattend to orignal
                t1.prev=curr #linking of first node of flattend to orignal
                curr.child=None #no need of child
            curr=curr.next #aage badho
        return head     #return orignal head
            
            
        
       
        