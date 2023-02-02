# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(-1) #just to be sure ki first element se execution ho
        dummy.next=head #insert dummy in beginning
        head=dummy #make dummy as new head
        thead=head  
        while thead.next!=None:
            if thead.next.val==val:
                thead.next=thead.next.next
            else:
                thead=thead.next
        return head.next       #since head to dummy hai actual list next se shuru hai
        