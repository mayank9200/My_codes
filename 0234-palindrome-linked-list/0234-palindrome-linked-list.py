# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self,curr):
        prev=None
        while curr!=None:
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
        return prev    
            
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head==None or head.next==None:
            return head
        h1=head
        slow=head
        fast=head.next #even me first wala chhiye
        while fast!=None and fast.next!=None: #find mid
            slow=slow.next
            fast=fast.next.next
        h2=self.rev(slow)
        slow.next=None #important, list ko do half me divide
        while h1!=None and h2!=None: #check both list individually
            if h1.val!=h2.val:
                return False
            h1=h1.next
            h2=h2.next
        return True    
        
        