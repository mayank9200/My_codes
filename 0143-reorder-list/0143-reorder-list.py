# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #do again
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        curr = head
        while len(stack) > 2:
            temp = curr.next
            curr.next = stack.pop()
            curr.next.next = temp
            curr = temp
            stack.pop(0)
        stack[-1].next = None

           
        
        """
        Do not return anything, modify head in-place instead.
        """
        