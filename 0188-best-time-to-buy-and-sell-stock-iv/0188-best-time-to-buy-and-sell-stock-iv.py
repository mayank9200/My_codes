class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0 for i in range(n+1)] for j in range(k+1)]
        for i in range(1,k+1):
            maxx=float('-inf')
            for j in range(1,n+1):
                if dp[i-1][j-1]-prices[j-1]>maxx:
                    maxx=dp[i-1][j-1]-prices[j-1]
                dp[i][j]=max(dp[i][j],dp[i][j-1],maxx+prices[j-1],dp[i][j-1])
                        
        return dp[k][n]            
        