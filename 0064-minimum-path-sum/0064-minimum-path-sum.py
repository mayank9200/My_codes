class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #very simple
        m=len(grid)
        n=len(grid[0])
        dp=[[0 for i in range(n)] for j in range(m)]
        dp[0][0]=grid[0][0]
        for i in range(1,m):
            dp[i][0]=grid[i][0]+dp[i-1][0] #just increase byr previous
        for i in range(1,n):
            dp[0][i]=grid[0][i]+dp[0][i-1] #just increase by previous
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=grid[i][j]+min(dp[i-1][j],dp[i][j-1]) # that place +min before top or left
        #print(dp)        
        return dp[m-1][n-1]        
        
        