# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        thead1=headA
        thead2=headB
        while thead1!=thead2:
            thead1=thead1.next
            thead2=thead2.next
            if thead1==None and thead2==None:
                return None
            if thead1==None:
                thead1=headB
            if thead2==None:
                thead2=headA
        return thead1        
            