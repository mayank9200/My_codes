# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
            
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None:
            return head
        i=0
        thead=head
        while i<k-1: # only to handle the case where length is less than k
            thead=thead.next
            if thead==None: #if before reaching k elements if thead becomes None means elements are less than k
                return head #dont reverse anything just return head as it is
            i+=1
        prev=None
        curr=head
        i=0
        while curr!=None and i<k:
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
            i+=1
        if curr!=None:
            head.next=self.reverseKGroup(curr,k)
        return prev    
        