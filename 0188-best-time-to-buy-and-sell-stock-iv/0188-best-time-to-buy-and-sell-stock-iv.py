class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        #https://www.youtube.com/watch?v=3YILP-PdEJA&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=35
        # def maxProfit(self, k: int, prices: List[int]) -> int:
        # n=len(prices)
        # dp=[[0 for i in range(n+1)] for j in range(k+1)]
        # for i in range(1,k+1):
        #     for j in range(1,n+1):
        #         for m in range(j-1,-1,-1): #from its above diagonal move till 0th index to bring max value upto there 
        #             dp[i][j]=max(dp[i][j],dp[i-1][m]+prices[j-1]-prices[m],dp[i][j-1])
        # return dp[k][n]    
        # The above code was getting tle but it is easy to understand so below one is just optimized soln
        n=len(prices)
        dp=[[0 for i in range(n+1)] for j in range(k+1)]
        for i in range(1,k+1):
            maxx=float('-inf')
            for j in range(1,n+1):
                if dp[i-1][j-1]-prices[j-1]>maxx: #maxx diff till now
                    maxx=dp[i-1][j-1]-prices[j-1]
                dp[i][j]=max(dp[i][j],dp[i][j-1],maxx+prices[j-1],dp[i][j-1]) #optimized
                        
        return dp[k][n]            
        