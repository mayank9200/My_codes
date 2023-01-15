class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        j=0
        n=len(nums)
        summ=0
        minn=float('inf')
        while j<n:
            summ=summ+nums[j]
            while summ>=target:
                minn=min(minn,j-i+1)
                summ-=nums[i]
                i+=1
            j+=1    
        if minn==float('inf'):
            return 0
        return minn
        
            
        