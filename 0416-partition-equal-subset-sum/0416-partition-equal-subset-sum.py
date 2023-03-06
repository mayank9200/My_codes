class Solution:
    def check(self,nums,n,summ,dp):
        if n==0:
            return False
        # if summ<0:
        #     return False
        if summ==0:
            return True
        if dp[n][summ]!=-1:
            return dp[n][summ]
        if nums[n-1]<=summ:
            dp[n][summ]=self.check(nums,n-1,summ-nums[n-1],dp) or self.check(nums,n-1,summ,dp)
            return dp[n][summ]
        else:
            dp[n][summ]=self.check(nums,n-1,summ,dp)
            return dp[n][summ]
            
    def canPartition(self, nums: List[int]) -> bool:
        summ_of_nums=sum(nums)
        if summ_of_nums%2!=0:
            return False
        dp=[[-1 for i in range(summ_of_nums//2+1)] for j in range(len(nums)+1)]
        #print(dp)
        return self.check(nums,len(nums),summ_of_nums//2,dp)
        
        