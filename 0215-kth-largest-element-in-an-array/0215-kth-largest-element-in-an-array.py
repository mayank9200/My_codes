class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heappush,heappop
        h=[]
        for i in nums:
            heappush(h,i)
            if len(h)>k:
                heappop(h)
        return h[0]        
        