class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        i=0
        summ=0
        while i+1<n:
            #print(nums[i],nums[i+1])
            summ+=min(nums[i],nums[i+1])
            i=i+2
        return summ  
        