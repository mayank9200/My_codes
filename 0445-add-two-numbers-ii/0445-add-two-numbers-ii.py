# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        if head==None:
            return None
        curr=head
        prev=None
        while curr!=None:
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
        return prev    
            
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        thead=ListNode(-1)
        fhead=thead
        carry=0
        l1=self.reverse(l1)
        l2=self.reverse(l2)
        while l1!=None and l2!=None:
            val=l1.val+l2.val+carry
            if val>9:
                val=val%10
                carry=1
            else:
                carry=0
            temp=ListNode(val)
            thead.next=temp
            thead=thead.next
            l1=l1.next
            l2=l2.next
        while l1!=None:
            val=l1.val+carry
            if val>9:
                val=val%10
                carry=1
            else:
                carry=0
            temp=ListNode(val)
            thead.next=temp
            thead=thead.next
            l1=l1.next
        while l2!=None:
            val=l2.val+carry
            if val>9:
                val=val%10
                carry=1
            else:
                carry=0
            temp=ListNode(val)
            thead.next=temp
            thead=thead.next
            l2=l2.next  
        if carry==1:
            thead=fhead
            while thead.next!=None:
                thead=thead.next
            thead.next=ListNode(1)    
        return self.reverse(fhead.next)
        