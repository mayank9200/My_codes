class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max=float('-inf')
        over_max=float('-inf')
        for i in nums:
            cur_max=max(cur_max+i,i)
            over_max=max(over_max,cur_max)
        return over_max 
            
        