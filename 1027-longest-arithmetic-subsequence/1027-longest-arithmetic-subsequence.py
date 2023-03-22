class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[{} for i in range(n)]
        maxx=0
        for i in range(n):
            for j in range(i):
                val=nums[i]-nums[j]
                if val in dp[j]:
                    dp[i][val]=dp[j][val]+1
                else:
                    dp[i][val]=1
                maxx=max(maxx,dp[i][val])      
        #print(dp)
        return maxx+1        
        