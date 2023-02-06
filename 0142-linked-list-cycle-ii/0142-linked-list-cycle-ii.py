# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first=head
        second=head
        while second!=None and second.next!=None:
            first=first.next
            second=second.next.next
            if first==second:
                break
        if second==None or second.next==None:
            return None
        first=head #start from beginning
        while first!=second: #when they meet again
            first=first.next
            second=second.next
        return first  
        