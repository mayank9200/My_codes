# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        thead=head
        while thead.next!=None:
            if thead.val==thead.next.val:
                thead.next=thead.next.next
            else:
                thead=thead.next
        return head        
            
        