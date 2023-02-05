# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        dummy.next=head
        prev=dummy
        curr=head
        while curr!=None and curr.next!=None:
            if curr.val!=curr.next.val:
                prev=prev.next
                curr=curr.next
            else:
                tval=curr.val
                while curr!=None and curr.val==tval:
                    curr=curr.next
            prev.next=curr
        return dummy.next    
        