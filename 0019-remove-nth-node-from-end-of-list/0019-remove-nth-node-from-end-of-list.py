# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if fast==None: #if fast is the last element 
            return head.next
        while fast.next!=None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
        
        