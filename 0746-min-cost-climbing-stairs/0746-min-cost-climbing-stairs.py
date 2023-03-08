class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[0 for i in range(n)] #see till n step 
        if n<=2:
            return min(cost[0],cost[1]) #to ease the loop
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,n): #traverse and and at point store how much is cost required to reach at that point
            dp[i]=min(dp[i-1]+cost[i],dp[i-2]+cost[i]) 
        return min(dp[n-1],dp[n-2])  #reaching last is min of last two
        