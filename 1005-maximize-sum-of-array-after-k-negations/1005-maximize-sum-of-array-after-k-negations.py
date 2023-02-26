class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
        for i in range(n):
            if k==0:
                break
            if nums[i]<0:
                nums[i]=-1*nums[i]
                k=k-1
        minn=float('inf')  
        summ=0
        for i in range(n):
            summ+=nums[i]
            minn=min(minn,nums[i])
        if k%2!=0:
            return summ-2*minn
        else:
            return summ            
        
                