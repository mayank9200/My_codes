class Solution:
    def solve(self,coins,n,amount,dp):
        if n==0:
            return float('inf')
        if amount==0:
            return 0
        if dp[n][amount]!=-1:
            return dp[n][amount]
        if coins[n-1]<=amount:
            dp[n][amount]=min(1+self.solve(coins,n,amount-coins[n-1],dp),self.solve(coins,n-1,amount,dp))
        else:
            dp[n][amount]=self.solve(coins,n-1,amount,dp)
        return dp[n][amount]                             
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[-1 for i in range(amount+1)]for j in range(n+1)]
        ans=self.solve(coins,n,amount,dp)
        if ans==float('inf'):
            return -1
        return ans
        