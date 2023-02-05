# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,curr,n):
        i=0
        prev=None
        temp=curr
        while curr!=None and i<n:
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
            i+=1
        return (temp,prev,curr)    
            
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(-1)
        dummy.next=head
        head=dummy
        curr=head
        i=1
        while curr!=None and i<left:
            curr=curr.next
            i+=1
        # print(curr.val)    
        h1,h2,h3=self.reverse(curr.next,right-left+1)
        #print(h1.val,h2.val,h3.val)
        curr.next=h2
        h1.next=h3
        return head.next
        
                
            
            
        
        