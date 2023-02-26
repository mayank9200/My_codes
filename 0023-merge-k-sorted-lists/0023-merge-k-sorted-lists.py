# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heappush,heappop
        h=[]
        n=len(lists)
        for i in range(n):
            if lists[i]!=None:
                heappush(h,[lists[i].val,i,lists[i]])
        ans=ListNode(-1)
        res=ans
        while len(h)>0:
            val,counter,node=heappop(h)
            ans.next=node
            ans=node
            if node.next!=None:
                heappush(h,[node.next.val,counter+100,node.next])
        return res.next        
            
            