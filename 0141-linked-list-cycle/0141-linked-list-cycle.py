# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first=head
        second=head
        while second!=None and second.next!=None:
            first=first.next
            second=second.next.next
            if first==second:
                return True
        return False    
        