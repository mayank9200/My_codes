# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        curr=head.next.next
        prev=head
        head=head.next
        head.next=prev
        prev.next=None
        while curr!=None and curr.next!=None:
            nextt=curr.next.next
            prev.next=curr.next
            curr.next.next=curr
            prev=curr
            curr=nextt
        prev.next=curr
        return head
        
        
        