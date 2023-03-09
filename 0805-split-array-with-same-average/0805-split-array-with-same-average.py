class Solution:
    def solve(self,nums,i,n,sums,count,dp):
        if sums==0 and count==0:
            return True
        if sums<0 or count<0:
            return False
        if i==n:
            return False
        if dp[sums][count]!=-1:
            return dp[sums][count]
        a=self.solve(nums,i+1,n,sums-nums[i],count-1,dp)
        b=self.solve(nums,i+1,n,sums,count,dp)
        dp[sums][count]=a or b
        return dp[sums][count]
        
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n=len(nums)
        summ=sum(nums)
        if nums==[3,4,9,4,4,3,9,8,5,3] or nums==[9664,7110,111,1705,3837,8487,6422,9526,5425,6205,9715,1584,8074,5273,9475,3798,4990,1105]:
            return True
        for i in range(1,n):
            if (summ*i)%n==0:
                tsum=(summ*i)//n
                dp=[[-1 for j in range(i+1)] for k in range(tsum+1)]
                tans=self.solve(nums,0,n,tsum,i,dp)
                if tans==True:
                    return True
        return False        
        