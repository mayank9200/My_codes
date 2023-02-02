# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sodd=ListNode(-1)
        seven=ListNode(-1)
        eodd=sodd
        eeven=seven
        curr=head
        flag=True
        while curr!=None:
            if flag==True:
                eodd.next=curr
                eodd=eodd.next
                curr=curr.next
                flag=False
            else:
                eeven.next=curr
                eeven=eeven.next
                curr=curr.next
                flag=True
        eodd.next=seven.next
        eeven.next=None
        return sodd.next
                
        