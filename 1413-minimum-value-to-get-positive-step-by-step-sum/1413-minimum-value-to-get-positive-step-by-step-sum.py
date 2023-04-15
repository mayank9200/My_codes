class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minn=float('inf')
        pre=0
        for i in nums:
            pre+=i
            minn=min(minn,pre)
        
        if minn>0:
            return 1
        return -(minn-1)    
        