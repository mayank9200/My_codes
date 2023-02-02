# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        c1=0
        curr1=headA
        while curr1!=None:
            c1+=1
            curr1=curr1.next
        c2=0
        curr2=headB
        while curr2!=None:
            c2+=1
            curr2=curr2.next
        if c1>=c2:
            i=0
            while headA!=None and i<(c1-c2):
                headA=headA.next
                i+=1
        else:
            i=0
            while headB!=None and i<(c2-c1):
                headB=headB.next
                i+=1      
        #print(headA,headB)        
        while headA!=None and headB!=None and headA!=headB:
            headA=headA.next
            headB=headB.next
        return headA    