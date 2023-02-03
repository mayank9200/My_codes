"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #inserting a new node after every node with same val
        if head==None:
            return None
        curr=head
        while curr!=None:
            nextt=curr.next
            curr.next=Node(curr.val)
            curr.next.next=nextt
            curr=nextt
        curr=head
        while curr!=None:
            if curr.random!=None:
                curr.next.random=curr.random.next
            else:
                curr.next.random=None
            curr=curr.next.next
        curr=head.next
        while curr!=None and curr.next!=None:
            curr.next=curr.next.next
            curr=curr.next
        return head.next    
            
        