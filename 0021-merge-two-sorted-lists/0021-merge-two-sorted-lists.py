# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nhead=ListNode(-1)
        fhead=nhead
        while list1!=None and list2!=None:
            if list1.val<list2.val:
                nhead.next=list1
                list1=list1.next
                nhead=nhead.next
            else:
                nhead.next=list2
                list2=list2.next
                nhead=nhead.next
        while list1!=None:
                nhead.next=list1
                list1=list1.next
                nhead=nhead.next
        while list2!=None:
                nhead.next=list2
                list2=list2.next
                nhead=nhead.next
        return fhead.next     
                
                
                