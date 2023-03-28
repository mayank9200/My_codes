class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[1 for i in range(n+1)]
        for i in range(2,n+1):
            if i!=n:
                maxx=i
            else:
                maxx=0
            start=1
            end=i-1
            while start<=end:
                maxx=max(maxx,dp[start]*dp[end])
                start+=1
                end-=1
            dp[i]=maxx
        return dp[n]    
                
        