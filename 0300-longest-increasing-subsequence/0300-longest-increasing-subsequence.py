class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0 for i in range(n)]
        dp[0]=1
        for i in range(1,n):
            maxx=0
            for j in range(i):
                if nums[i]>nums[j]:
                    maxx=max(maxx,dp[j])
            dp[i]=maxx+1
        return max(dp)    
                    
            