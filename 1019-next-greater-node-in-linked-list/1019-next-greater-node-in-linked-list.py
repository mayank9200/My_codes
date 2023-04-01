# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        curr=head
        prev=None
        while curr!=None:
            nextt=curr.next
            curr.next=prev
            prev=curr
            curr=nextt
        return prev    
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        from collections import deque
        nhead=self.reverse(head)
        s=deque()
        ans=[]
        while nhead!=None:
            if len(s)!=0 and s[0]>nhead.val:
                ans.append(s[0])
                s.appendleft(nhead.val)
            else:
                while len(s)>0 and s[0]<=nhead.val:
                    s.popleft()
                if len(s)==0:
                    ans.append(0)
                else:
                    ans.append(s[0])
                s.appendleft(nhead.val)
            nhead=nhead.next    
        return ans[::-1]
        
        