class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0 for i in range(n)] # meaning is at d[i] contains LIS considering i as last element
        dp[0]=1
        for i in range(1,n):
            maxx=0
            for j in range(i):
                if nums[i]>nums[j]: #if element is smaller then current
                    maxx=max(maxx,dp[j]) #see what was the max increasing subsequence till that point and add 1
            dp[i]=maxx+1 #final ans till that point will be maxx till prev +1
        return max(dp)     
                    
            