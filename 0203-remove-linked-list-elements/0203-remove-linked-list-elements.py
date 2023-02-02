# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head==None:
            return None
        thead=head
        while thead.next!=None:
            if thead.next.val==val:
                thead.next=thead.next.next
            else:
                thead=thead.next
        if head.val==val:
            return head.next
        return head        
        