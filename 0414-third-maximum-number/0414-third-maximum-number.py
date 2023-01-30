class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        from heapq import heappush,heappop
        h=[]
        nums=list(set(nums)) #distinct elements
        print(nums)
        if len(nums)<3:
            return max(nums)
        for i in nums:
            heappush(h,i)
            if len(h)>3:
                heappop(h)
        return h[0]        